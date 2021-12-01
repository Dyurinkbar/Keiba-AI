'''競走馬のデータを取得'''
import requests
from bs4 import BeautifulSoup as bs
import RaceResult
import re

import Horse
import utils.StringUtils as StringUtils


# 競走馬全頭のデータを取得
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


# 競走馬のレース情報を取得
def get_horse_data_of_race_results(horse: Horse):
    # 競走馬オブジェクトから成績URLを取得
    grade_url = horse.get_grade_url()
    # URLからHTMLを取得
    res = requests.get(grade_url)
    soup = bs(res.content, "html.parser")
    # 競走成績表を取得
    grade_table = soup.find(class_=re.compile(
        "db_")).select_one("tbody")

    # 取得したデータをセット
    races = []
    # trタグ毎に読む
    for grade_element in grade_table:
        # レースデータオブジェクトを生成
        race = RaceResult.RaceResult()
        # tdタグを順に読む
        for n in range(len(grade_element)):
            # race.set_date(grade_element[n].select("td")[0].text)
            print(StringUtils.replace_not_blank(
                grade_element[n].select("td")[0].text))
        races.append(race)
    return races


# レース情報を表示
def print_race_data(race: RaceResult):
    print("日付：" + race.get_date())
    print("開催場所：" + race.get_venue())
    print("天気：" + race.get_weather())
    print("レース名：" + race.get_race_name())
    print("出馬頭数：" + race.get_horse_head_count())
    print("枠：" + race.get_waku())
    print("馬番：" + race.get_umaban())
    print("着順：" + race.get_rank())
    print("鞍上：" + race.get_jockey())
    print("斤量：" + race.get_penalty_weight())
    print("距離：" + race.get_distance())
    print("馬場状態：" + race.get_race_situation())
    print("タイム：" + race.get_time())
    print("着差：" + race.get_reach_difference())
    print("通過着順：" + race.get_passing_ranks())
    print("上がりタイム：" + race.get_final_time())
    print("馬体重：" + race.get_body_weight())
