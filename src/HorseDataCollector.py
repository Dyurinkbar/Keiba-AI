'''競走馬のデータを取得'''
from bs4 import BeautifulSoup as bs
import re
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

import instance.Horse as Horse
import instance.RaceDetail as RaceDetail
import instance.RaceResult as RaceResult
import utils.SoupUtils as SoupUtils
import utils.StringUtils as StringUtils


# 競走馬全頭のレース周りのデータを取得
# 解析目標のレース情報の詳細も同時に取得
def get_horses_data_of_status(soup: bs):
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
    horse_grade_url = soup.select("span[class^=HorseName] a")

    horses = []
    for n in range(len(horse_list)):
        # インスタンス生成
        horse = Horse.Horse()
        # 情報をセット
        horse.set_waku(horse_waku[n].text)
        horse.set_umaban(horse_umaban[n].text)
        horse.set_name(horse_name[n].text)
        horse.set_seirei(horse_seirei[n].text)
        horse.set_penalty_weight(horse_penalty_weight[n].text)
        horse.set_jockey(StringUtils.replace_not_blank(jockey_name[n].text))
        horse.set_trainer_place(horse_trainer_place[n].text)
        horse.set_grade_url(horse_grade_url[n].attrs['href'])
        horses.append(horse)
    return horses


# 競走馬のレース成績を取得
def get_horse_data_of_race_results(race_results_url: str):
    # URLからHTMLを取得
    soup = SoupUtils.get_soup(race_results_url)
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
        results_data = race_result.select("td")
        # 日付
        race.set_date(StringUtils.replace_not_blank(
            results_data[0].text))
        # 開催場所
        race.set_venue(StringUtils.replace_not_blank(
            results_data[1].text))
        # 天気
        race.set_weather(StringUtils.replace_not_blank(
            results_data[2].text))
        # レース名
        race.set_race_name(StringUtils.replace_not_blank(
            results_data[4].text))
        # 出馬頭数
        race.set_horse_head_count(StringUtils.replace_not_blank(
            results_data[6].text))
        # 枠
        race.set_waku(StringUtils.replace_not_blank(
            results_data[7].text))
        # 馬番
        race.set_umaban(StringUtils.replace_not_blank(
            results_data[8].text))
        # 着順
        race.set_rank(StringUtils.replace_not_blank(
            results_data[11].text))
        # 鞍上
        race.set_jockey(StringUtils.replace_not_blank(
            results_data[12].text))
        # 斤量
        race.set_penalty_weight(StringUtils.replace_not_blank(
            results_data[13].text))
        # 距離
        race.set_race_distance(StringUtils.replace_not_blank(
            results_data[14].text))
        # 馬場状態
        race.set_race_condition(StringUtils.replace_not_blank(
            results_data[15].text))
        # タイム
        race.set_time(StringUtils.replace_not_blank(
            results_data[17].text))
        # 着差
        race.set_reach_difference(StringUtils.replace_not_blank(
            results_data[18].text))
        # 通過着順
        race.set_passing_ranks(StringUtils.replace_not_blank(
            results_data[20].text))
        # 上がりタイム
        race.set_final_time(StringUtils.replace_not_blank(
            results_data[22].text))
        # 馬体重
        race.set_body_weight(StringUtils.replace_not_blank(
            results_data[23].text))
        # リストに追加
        races.append(race)
    return races


# 上位のリーディングジョッキー取得(引数:上位の人数)
def get_leading_jockey(jockey_count: int):
    # データベースの騎手リーディングページのHTMLを取得
    soup = SoupUtils.get_soup("https://db.netkeiba.com/?pid=jockey_leading")

    # データの取得
    jockey_names = soup.find_all(
        href=re.compile("/jockey/"), limit=jockey_count)

    # 上位リーディングジョッキーを格納する配列を宣言(昇順)
    leading_jockeys = []
    # 取得したジョッキーをリストに追加
    [leading_jockeys.append(jockey_name) for jockey_name in jockey_names]

    return leading_jockeys
    # 東西の情報も入れたい(Dictionary<jockey,place>)


# 過去のレースデータを取得(引数:レース名,年数)
# ドロップボタンで年を選択→表示をクリック→レースのURL取得→の繰り返し
def get_past_race_data(race_name: str, years: int):
    print("Seleniumを使用します。")

    # Webドライバーのオプションを設定(ウィンドウを開かなくする)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    # Webドライバー生成
    driver = webdriver.Chrome(options=options)

    # 重賞日程ページURLからHTMLを取得
    driver.get("https://race.netkeiba.com/top/schedule.html")

    # 年を設定しているドロップボタンを取得
    dropdown = driver.find_element_by_id("select-order")
    # 「表示」ボタンを取得
    button = driver.find_element_by_class_name("Submit_Btn btn")

    # セレクトオブジェクト生成
    select = Select(dropdown)

    # 過去レースのリスト宣言
    past_race_data = []

    # 引数の年数分、過去のレースのURLを取得
    for n in range(years):
        # 一つ前の年を選択
        select.select_by_index(len(select.options)(n - 1))
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
                # past_race_data.append(race_url)
                break

    # ドライバークローズ
    driver.close()
    return past_race_data
    # レース名が一致しない可能性があるので、重賞日程ページと同じ表記にする必要がある
