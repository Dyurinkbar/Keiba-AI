'''競馬AIのメインクラス'''
import requests
from bs4 import BeautifulSoup as bs

import Horse
import HorseDataCollector
import utils.SoupUtils as SoupUtils
import utils.StringUtils as StringUtils
import utils.FileUtils as FileUtils


# Main
def main():
    # テスト用URL (2021年 日本ダービー)
    url = "https://race.netkeiba.com/race/shutuba.html?race_id=202105021211"

    # URLを入力
    # url = input_race_url()

    # URLからHTMLを取得
    soup = SoupUtils.get_soup(url)

    # CUIに取得したHTNLを出力
    # SoupUtils.print_all_html(soup)

    # 整形したHTMLをtxtに出力
    # FileUtils.file_writer(str(soup.prettify()), "html_prettify.txt")

    # 競走馬オブジェクトを生成
    print("\n競走馬オブジェクトを生成します。")
    horses = HorseDataCollector.get_horses_data_of_status(soup)
    print("\n競走馬オブジェクトを生成しました。")

    # 競走馬の情報を表示
    print_horse_data(horses)

    # 競走毎に成績データオブジェクトを生成
    print("\nレース成績オブジェクトを生成します。")
    for n in range(len(horses)):
        race_results = HorseDataCollector.get_horse_data_of_race_results(
            horses[n].get_grade_url())
        # 競走馬オブジェクトにレース成績をセット
        horses[n].set_race_results(race_results)
    print("\nレース成績オブジェクトを生成しました。")

    # 競走馬のレース成績を表示
    print_race_results(horses)


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


# 競走馬の情報を出力
def print_horse_data(horses: Horse):
    print("\n---競走馬の情報---\n")
    for horse in horses:
        horse.print_horse_data()


# 競走馬のレース成績を表示
def print_race_results(horses: Horse):
    print("\n---レース戦績---\n")
    for horse in horses:
        print(horse.get_name())
        race_results = horse.get_race_results()
        for race_result in race_results:
            race_result.print_race_result_data()


if __name__ == "__main__":
    main()
