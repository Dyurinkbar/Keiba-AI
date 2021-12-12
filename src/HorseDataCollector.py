"""競走馬のデータを取得"""
from bs4 import BeautifulSoup as bs
import re
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

import instance.Horse as Horse
import instance.RaceDetail as RaceDetail
import instance.RaceResult as RaceResult
import instance.RaceResultDB as RaceResultDB
import utils.SoupUtils as SoupUtils
import utils.StringUtils as StringUtils
import utils.HorseDataUtils as HorseDataUtils


# 競走馬全頭のレース周りのデータを取得
def get_horses_data_of_status_by_main_race(main_race_url: str):
    print("\n出走馬のデータを出馬表から取得します。")
    # HTNL取得
    soup = SoupUtils.get_soup(main_race_url)

    '''データ取得'''
    # 競走馬のリストを取得
    horse_list = soup.select("tr.HorseList")
    # 枠
    horse_waku = soup.select("td[class^=Waku] span")
    # 馬番
    horse_umaban = soup.select("td[class^=Umaban]")
    # 馬名
    horse_name = soup.find_all(
        href=re.compile("https://db.netkeiba.com/horse/"))
    # 性齢
    horse_seirei = soup.select("td[class^=Barei]")
    # 斤量
    horse_penalty_weight = soup.select("td[class^=Barei] + td")
    # 厩舎場所
    horse_trainer_place = soup.select("td[class^=Trainer] span")
    # 鞍上
    jockey_name = soup.select("td[class^=Jockey]")
    # 競走成績URL
    race_results_url = soup.select("span[class^=HorseName] a")

    horses = []
    for n in range(len(horse_list)):
        # インスタンス生成
        horse = Horse.Horse()
        # 情報をセット
        horse.waku = horse_waku[n].text
        horse.umaban = horse_umaban[n].text
        horse.name = horse_name[n].text
        horse.seirei = horse_seirei[n].text
        horse.penalty_weight = horse_penalty_weight[n].text
        horse.jockey = StringUtils.replace_shave_blank(jockey_name[n].text)
        horse.trainer_area = horse_trainer_place[n].text
        horse.race_results_url = race_results_url[n].attrs['href']
        horses.append(horse)

    print("取得しました。\n")
    return horses


# 競走馬のDBから取得できるデータを抽出
def get_horses_data_of_status_by_database(horses: Horse):
    print("\n出走馬のデータをデータベースから取得します。")

    for horse in horses:
        print(f"{StringUtils.replace_shave_blank(horse.name)} から取得")
        # URLからHTMLを取得
        soup = SoupUtils.get_soup(horse.race_results_url)

        # プロフィール部分取得
        profile = soup.find(class_=re.compile(
            "db_prof_area_02")).find("table")

        # 生年月日
        horse.birthday = profile.find_all("td")[0].text
        # 調教師
        horse.trainer = profile.find("a", href=re.compile("/owner/")).text
        # 馬主
        horse.owner = profile.find("a", href=re.compile("/owner/")).text
        # 生産者
        horse.breeder = profile.find(
            "a", href=re.compile("/breeder/")).text

        # 血統部分取得
        edigrees = soup.find(class_="blood_table").find_all("a")
        # 血統
        edigree_dict = {
            "父": edigrees[0].text, "母": edigrees[1].text,
            "父父": edigrees[2].text, "父母": edigrees[3].text,
            "母父": edigrees[4].text, "母母": edigrees[5].text
        }
        horse.edigrees = edigree_dict
    print("取得しました。\n")
    return horses


# レースの情報を出馬表から取得
def get_race_data_of_main_race(main_race_url: str):
    print("\nレースの情報を出馬表から取得します。")
    # HTNL取得
    soup = SoupUtils.get_soup(main_race_url)

    # レースオブジェクト生成
    race_detail = RaceDetail.RaceDetail()

    # レース名取得
    race_detail.race_name = StringUtils.replace_shave_blank(
        soup.select_one("div.RaceName").text)

    # レースURLをセット
    race_detail.race_url = main_race_url

    # 1行目の箇所取得
    data_line1 = soup.find("div", class_="RaceData01")

    # 距離(起点)の箇所を取得
    distance_part = data_line1.find("span")
    # 距離と馬場
    race_detail.distance_and_racetrack = StringUtils.replace_shave_blank(distance_part.text)

    # 内外回りと天候の箇所を取得
    around_part = distance_part.next_sibling

    around = ""
    # 天候は解析日によって表示されていない可能性があるので、チェック
    try:
        # 内外回りと天候をスラッシュで分割
        strs = around_part.split("/")
        around = strs[0]
        weather = strs[1]
        # 天候
        race_detail.weather = weather.split(":")[1]
    except:
        print("天候は存在しないか取得できません。")
        # 内外回りは存在するので、取得
        around = around_part

    # 周回方向
    race_detail.around = StringUtils.replace_shave_parentheses(around)

    # 馬場状態の箇所を取得
    race_condition = data_line1.select("span[class^=Item04]")
    # 解析日によって表示されていない可能性があるので、チェック
    try:
        # 馬場状態
        race_detail.race_condition = race_condition[0].text.split("馬場:")[1]
    except:
        print("馬場状態は存在しないか取得できません。")

    # 2行目の箇所取得
    data_line2 = soup.find("div", class_="RaceData02").find_all("span")

    # tagがないので、順に取得
    # 開催場所
    race_detail.venue = data_line2[1].text
    # 出馬条件
    race_detail.entry_terms = data_line2[3].text
    # クラス
    race_detail.grade = data_line2[4].text
    # 斤量設定
    race_detail.penalty_weight_setting = data_line2[6].text
    # 出馬頭数
    race_detail.horse_head_count = data_line2[7].text

    print("取得しました。\n")
    return race_detail


# 競走馬のレース成績を取得
def get_horse_data_of_race_results(race_results_url: str):
    print("\n出走馬の競走成績を取得します。")

    # URLからHTMLを取得
    soup = SoupUtils.get_soup(race_results_url)

    # 馬の名前を取得し、表示
    horse_name = soup.select_one("div[class ^= horse_title] > h1").text
    print(f"{StringUtils.replace_shave_blank(horse_name)} から取得。")

    # 競走成績表を取得
    race_results = soup.find(class_=re.compile(
        "db_h_race")).find("tbody").find_all("tr", limit=1)

    # 取得したデータをセット
    races = []
    # trタグ毎に読む
    for race_result in race_results:
        # レースデータオブジェクトを生成
        race = RaceResult.RaceResult()
        # tdタグを順に読む
        results_data = race_result.find_all("td")
        # 日付
        race.date = StringUtils.replace_shave_blank(
            results_data[0].text)
        # 開催場所
        race.venue = StringUtils.replace_shave_blank(
            results_data[1].text)
        # 天気
        race.weather = StringUtils.replace_shave_blank(
            results_data[2].text)
        # レース名
        race.race_name = StringUtils.replace_shave_blank(
            results_data[4].text)
        # レースURL
        race.race_url = "https://db.netkeiba.com" + results_data[4].find().attrs['href']
        # 出馬頭数
        race.horse_head_count = StringUtils.replace_shave_blank(
            results_data[6].text)
        # 枠
        race.waku = StringUtils.replace_shave_blank(
            results_data[7].text)
        # 馬番
        race.umaban = StringUtils.replace_shave_blank(
            results_data[8].text)
        # 着順
        race.rank = StringUtils.replace_shave_blank(
            results_data[11].text)
        # 鞍上
        race.jockey = StringUtils.replace_shave_blank(
            results_data[12].text)
        # 斤量
        race.penalty_weight = StringUtils.replace_shave_blank(
            results_data[13].text)
        # 距離
        race.race_distance = StringUtils.replace_shave_blank(
            results_data[14].text)
        # 馬場状態
        race.race_condition = StringUtils.replace_shave_blank(
            results_data[15].text)
        # タイム
        race.time = StringUtils.replace_shave_blank(
            results_data[17].text)
        # 着差
        race.reach_difference = StringUtils.replace_shave_blank(
            results_data[18].text)
        # 通過着順
        race.passing_ranks = StringUtils.replace_shave_blank(
            results_data[20].text)
        # ペース
        race.pace = StringUtils.replace_shave_blank(
            results_data[21].text)
        # 上がりタイム
        race.final_rap_time = StringUtils.replace_shave_blank(
            results_data[22].text)
        # 馬体重
        race.body_weight = StringUtils.replace_shave_blank(
            results_data[23].text)
        # リストに追加
        races.append(race)

    print("取得しました。\n")
    return races


# DBのレース結果から、レース情報を取得
def get_race_results_by_database(race_db_url: str):
    print("\nデータベースからレース情報を取得します。")

    # レースDBのHTML取得
    soup = SoupUtils.get_soup(race_db_url)

    # レース情報オブジェクトとレースDBリスト生成
    race_detail = RaceDetail.RaceDetail()
    race_results_db: RaceResultDB = []

    # レース情報を取得
    race_detail_part = soup.find("dl", class_="racedata fc")

    # レース名
    race_detail.race_name = StringUtils.replace_shave_blank(
        race_detail_part.find("h1").text)
    # レースURL
    race_detail.race_url = race_db_url
    # レースのクラスをタイトルから調べる

    # レース情報部分の取得1
    race_data_part1 = race_detail_part.find("p").find("span").text

    # 取得した文字列を切り取る
    race_data_strs = race_data_part1.split("/")

    # 距離と馬場の文字に混入している文字を削る
    distance_and_racetrack = StringUtils.replace_shave_designated(
        race_data_strs[0], ["左", "右", "内", "外", "直", "線"])

    # 距離と馬場
    race_detail.distance_and_racetrack = StringUtils.replace_shave_blank(distance_and_racetrack)

    # 天候
    race_detail.weather = StringUtils.replace_shave_blank(race_data_strs[1].split(": ")[1])
    # 馬場状態
    race_detail.race_condition = StringUtils.replace_shave_blank(race_data_strs[2].split(": ")[1])

    # レース情報部分の取得2
    race_data_part2 = soup.find(
        "p", class_=re.compile("smalltxt")).text

    # 取得した文字列を切り取る
    race_data_strs = race_data_part2.split(" ")

    # 開催日
    race_detail.date = StringUtils.replace_date_to_slash(race_data_strs[0])

    # 開催場所(２文字の地名しかないので妥協)
    venue = race_data_strs[1].split("回")[1][0:2]
    race_detail.venue = venue
    # 内外回り
    race_detail.around = HorseDataUtils.get_around_from_venue(venue)

    # 出馬条件
    race_detail.entry_terms = StringUtils.replace_shave_blank(race_data_strs[2].split("(")[0])

    # 斤量設定
    pws = race_data_strs[2].split("(")[3].split(")")[0]
    race_detail.penalty_weight_setting = pws

    # レース結果部分を取得
    race_results_db_part = soup.find("table",
                                     class_=re.compile("race_table_01 nk_tb_common")).find_all("tr")

    # レース結果部分の取得要素数が競走馬の出馬頭数なので、セット
    race_detail.horse_head_count = len(race_results_db_part)

    '''レース結果取得'''
    for n in range(len(race_results_db_part)):
        # 0要素目はヘッダー情報なので飛ばす
        if n == 0:
            continue

        # tdタグをすべて取得
        race_results_db_part_td_tags = race_results_db_part[n].find_all("td")

        # レースDB情報オブジェクト生成
        race_result_db = RaceResultDB.RaceResultDB()

        # 着順
        race_result_db.rank = (StringUtils.replace_shave_blank(
            race_results_db_part_td_tags[0].text))
        # 枠
        race_result_db.waku = (StringUtils.replace_shave_blank(
            race_results_db_part_td_tags[1].text))
        # 馬番
        race_result_db.umaban = (StringUtils.replace_shave_blank(
            race_results_db_part_td_tags[2].text))
        # 馬名
        race_result_db.horse_name = (StringUtils.replace_shave_blank(
            race_results_db_part_td_tags[3].text))
        # 競走成績URL
        race_result_db.race_results_url = ("https://db.netkeiba.com/" +
                                           race_results_db_part_td_tags[3].find("a").attrs['href'])
        # 性齢
        race_result_db.seirei = (StringUtils.replace_shave_blank(
            race_results_db_part_td_tags[4].text))
        # 斤量
        race_result_db.penalty_weight = (StringUtils.replace_shave_blank(
            race_results_db_part_td_tags[5].text))
        # 騎手
        race_result_db.jockey = (StringUtils.replace_shave_blank(
            race_results_db_part_td_tags[6].text))
        # タイム
        race_result_db.time = (StringUtils.replace_shave_blank(
            race_results_db_part_td_tags[7].text))
        # 着差
        race_result_db.reach_difference = (StringUtils.replace_shave_blank(
            race_results_db_part_td_tags[8].text))
        # 通過着順
        race_result_db.passing_ranks = (StringUtils.replace_shave_blank(
            race_results_db_part_td_tags[10].text))
        # 上りタイム
        race_result_db.final_rap_time = (StringUtils.replace_shave_blank(
            race_results_db_part_td_tags[11].text))
        # オッズ
        race_result_db.odds = (StringUtils.replace_shave_blank(
            race_results_db_part_td_tags[12].text))
        # 人気
        race_result_db.favorite = (StringUtils.replace_shave_blank(
            race_results_db_part_td_tags[13].text))
        # 馬体重
        race_result_db.body_weight = (StringUtils.replace_shave_blank(
            race_results_db_part_td_tags[14].text))
        # 厩舎地方
        race_result_db.trainer_area = (StringUtils.replace_shave_blank(
            race_results_db_part_td_tags[18].text))
        # 馬主
        race_result_db.owner = (StringUtils.replace_shave_blank(
            race_results_db_part_td_tags[19].text))

        # リストに格納
        race_results_db.append(race_result_db)

    print("取得しました。\n")
    return race_detail, race_results_db


# 上位のリーディングジョッキー取得(引数:上位の人数)
def get_leading_jockey(jockey_count: int):
    print(f"\nリーディングジョッキー上位{jockey_count}名を取得します。")

    # データベースの騎手リーディングページのHTMLを取得
    soup = SoupUtils.get_soup("https://db.netkeiba.com/?pid=jockey_leading")

    # データの取得
    jockey_names = soup.find_all(
        href=re.compile("/jockey/"), limit=jockey_count)

    # 上位リーディングジョッキーを格納する配列を宣言(昇順)
    leading_jockeys = []
    # 取得したジョッキーをリストに追加
    [leading_jockeys.append(jockey_name) for jockey_name in jockey_names]

    print("取得しました。\n")
    return leading_jockeys
    # 東西の情報も入れたい(Dictionary<jockey,place>)


# 過去のレースURLを取得(5年分だと思う)
# 出馬表の「データ分析」の下部の過去5年分のデータを取得
def get_past_race_url_by_data_analyze_page(main_race_url: str):
    print("\n過去レースのデータをデータ分析ページから取得します。")
    print("データ分析ページから過去データのURLを取得します。")

    # 過去レースのリスト宣言
    past_race_urls = []

    # 出馬表のURLを一部置き換えて、データ分析ページのURLを取得
    temp = main_race_url.split("shutuba")
    data_analyze_page_url = temp[0] + "data_top" + temp[1]
    # データ分析ページのHTMLを取得する
    soup = SoupUtils.get_soup(data_analyze_page_url)

    # 過去の成績の表部分を取得
    # past_race_part = soup.find("table",id="PastResultTable").find_all("tr")
    past_race_part = soup.find("div", class_="Table_Container")
    print(past_race_part)

    # レースのURL部分を取得
    past_race_url_parts = past_race_part.find_all(
        href=re.compile("https://db.netkeiba.com/race/"))
    print(past_race_url_parts)

    past_race_urls = past_race_url_parts.attrs['href']

    # データが取得できていたら、そのURLリストを返却
    # そうでなければ、重賞一覧からの取得に移る
    if past_race_urls[0] != "":
        print("取得しました。")
        return past_race_urls
    else:
        print("データ分析ページの過去データが見つかりませんでした。")
        return ""


# 過去のレースURLを取得(引数:レース名,年数)
# 「重賞日程」からドロップボタンで年を選択→表示をクリック→レースのURL取得→の繰り返し
def get_past_race_url_by_grade_race_schedule_page(race_name: str, years: int):
    print(f"\n過去レースのデータを重賞日程ページから {years} 年分取得します。")
    print("データ分析ページから過去データのURLを取得します。")
    print("Seleniumを使用します。")

    # レース名を重賞日程の名前と一致させる

    # Webドライバーのオプションを設定(ウィンドウを開かなくする)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    # Webドライバー生成
    driver = webdriver.Chrome(options=options)

    # 重賞日程ページURLからHTMLを取得
    driver.get("https://race.netkeiba.com/top/schedule.html")

    past_race_urls = []

    # 年を設定しているドロップボタンを取得
    dropdown = driver.find_element_by_id("select-order")
    # 「表示」ボタンを取得
    button = driver.find_element_by_class_name("Submit_Btn btn")

    # セレクトオブジェクト生成
    select = Select(dropdown)

    # 引数の年数分、過去のレースのURLを取得
    for n in range(years):
        # 一つ前の年を選択
        select.select_by_index(len(select.options(n - 1)))
        sleep(1)

        # 「表示」ボタンをクリック
        button.click()
        sleep(1)

        # レースURL部分を取得
        race_names = driver.find_elements_by_xpath(
            "//*[@id='Netkeiba_RaceTop']/div[1]/div/div[1]/div/div/div[2]/table/tbody/tr[2]/td[2]/a")

        # レース名が一致したURLをリストの追加
        for race_name in race_names.text:
            if race_name == race_name:
                # race_url = race_name.
                # past_race_urls.append(race_url)
                break

    # ドライバークローズ
    driver.close()
    print("取得しました。\n")
    return past_race_urls
    # レース名が一致しない可能性があるので、重賞日程ページと同じ表記にする必要がある
