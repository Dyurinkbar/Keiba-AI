'''競馬AIのメインクラス'''
import requests
from bs4 import BeautifulSoup as bs

import instance.Horse as Horse
import HorseDataCollector
from instance.RaceDetail import RaceDetail
from instance.RaceResultDB import RaceResultDB
import utils.SoupUtils as SoupUtils
import utils.StringUtils as StringUtils
import utils.FileUtils as FileUtils
import HorseDataPrinter


# Main
def main():
    # テスト用URL (2021年 日本ダービー)
    main_race_url = "https://race.netkeiba.com/race/shutuba.html?race_id=202105021211"

    # URLを入力
    # main_race_url = input_race_url()

    # 取得したHTNLを表示
    # SoupUtils.print_all_html(soup)

    # 整形したHTMLをtxtに出力
    # FileUtils.file_writer(str(soup.prettify()), "html_prettify.txt")
    # '''
    # 競走馬オブジェクトを生成
    horses: Horse = HorseDataCollector.get_horses_data_of_status_by_main_race(
        main_race_url)

    # レース情報を出馬表から取得
    race_detail: RaceDetail = HorseDataCollector.get_race_data_of_main_race(
        main_race_url)

    # 競走馬DBからデータを取得
    horses = HorseDataCollector.get_horses_data_of_status_by_database(horses)

    # 競走毎に成績データオブジェクトを生成
    for n in range(len(horses)):
        race_results = HorseDataCollector.get_horse_data_of_race_results(
            horses[n].get_race_results_url())
        # 競走馬オブジェクトにレース成績をセット
        horses[n].set_race_results(race_results)
    # '''

    '''
    # 過去レースのURLを取得
    # 「データ分析」ページから取得を試みる
    # 失敗したら、DBの「重賞日程」ページから取得
    past_race_urls = HorseDataCollector.get_past_race_url_by_data_analyze_page(
        main_race_url)
    
    if past_race_urls == "":
        past_race_urls = HorseDataCollector.get_past_race_url_by_grade_race_schedule_page(
            race_detail.get_race_name(), 5)
    print(past_race_urls)
    '''

    # レースDBから、レース情報を取得
    '''
    race_detail, race_results_db = HorseDataCollector.get_race_results_by_database(
        "https://db.netkeiba.com/race/202109050211/")'''

    # 競走馬の情報を表示
    HorseDataPrinter.print_horse_data(horses)

    # レースの情報を表示
    HorseDataPrinter.print_race_detail(race_detail)

    # 競走馬のレース成績を表示
    HorseDataPrinter.print_race_results(horses)

    # レースDBの情報を表示
    # HorseDataPrinter.print_race_results_db(race_results_db)


# URLを入力
def input_race_url():
    while(True):
        print("\nレースのURLを入力してください。\n→ ", end="")
        race_url = input()
        if str(race_url).contains("https://race.netkeiba.com/race/shutuba.html?race_id="):
            break
        else:
            print("\n入力エラーです。")
    return str(race_url)


if __name__ == "__main__":
    main()
