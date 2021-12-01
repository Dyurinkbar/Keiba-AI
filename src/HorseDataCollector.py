'''競走馬のデータを取得'''
from bs4 import BeautifulSoup as bs
import re

import Horse
import RaceResult
import utils.SoupUtils as SoupUtils
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
def get_horse_data_of_race_results(race_results_url: str):
    # URLからHTMLを取得
    soup = SoupUtils.get_soup(race_results_url)
    # 競走成績表を取得
    grade_table = soup.find(class_=re.compile(
        "db_h_race")).find("tbody").find_all("tr", limit=1)

    # 取得したデータをセット
    races = []
    # trタグ毎に読む
    for grade_element in grade_table:
        # レースデータオブジェクトを生成
        race = RaceResult.RaceResult()
        # tdタグを順に読む
        results_data = grade_element.select("td")
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
