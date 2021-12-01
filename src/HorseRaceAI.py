'''競馬AIのメインクラス'''
import requests
from bs4 import BeautifulSoup as bs

import Horse
import HorseDataCollector
import utils.StringUtils as StringUtils
import utils.PathUtils as PathUtils


# Main
def main():
    # テスト用URL (2021年 日本ダービー)
    url = "https://race.netkeiba.com/race/shutuba.html?race_id=202105021211"

    # URLを入力
    # url = input_race_url()

    # URLからHTMLを取得
    soup = get_soup(url)

    # CUIに取得したHTNLを出力
    # print_all_html(soup)

    # 整形したHTMLをtxtに出力
    # file_writer(str(soup.prettify()), "html_prettify.txt")

    # 競走馬オブジェクトを生成
    horses = HorseDataCollector.get_horses_data_of_status(soup)

    # 競走馬の情報を出力
    # print_horse_data(horses)

    # 競走毎に成績データオブジェクトを生成
    race = HorseDataCollector.get_horse_data_of_race_results(horses[0])
    '''
    for n in range(len(horses)):
        HorseDataCollector.get_horse_data_by_race(horses[n])
    '''


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


# URLからHTMLを取得
def get_soup(url: str):
    res = requests.get(url)
    soup = bs(res.content, "html.parser")
    return soup


# タイトルを取得
def get_title(soup: bs):
    return soup.title.text


# HTML全表示
def print_all_html(soup: bs):
    print(soup.prettify())


# 競走馬の情報を出力
def print_horse_data(horses: Horse):
    print("\n---競走馬の情報---\n")
    for horse in horses:
        horse.print_horse_data()


if __name__ == "__main__":
    main()
