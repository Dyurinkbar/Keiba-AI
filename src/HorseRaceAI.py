import requests
from bs4 import BeautifulSoup as bs
import re

import Horse
import StringUtil


# urlを入力
def input_race_url():
    print("\nレースのURLを入力してください。\n→ ", end="")
    race_url = input()
    return str(race_url)


# urlからBeautifulSoupを取得
def get_soup(url):
    res = requests.get(url)
    soup = bs(res.content, "html.parser")
    return soup


# HTML全表示
def print_all_html(soup):
    print(soup.prettify())


# 文字データをtxtに出力
def file_writer(content, file_name):
    txt_file = open(file_name, "w", encoding="UTF-8")
    txt_file.write(content)
    txt_file.close()


# 競走馬のデータを取得
def get_horse_status(soup):
    # 出馬表の部分を取得
    # shutuba_table = soup.find("table", class_=re.compile("^Shutuba_Table"))
    # shutuba_table = soup.select("table.Shutuba_Table.ShutubaTable")
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
        horse.set_jockey(StringUtil.replace_not_blank(jockey_name[n].text))
        horse.set_trainer_place(horse_trainer_place[n].text)
        horse.set_grade_url(horse_grade_url[n].attrs['href'])
        horses.append(horse)
    return horses


# 競走馬の情報を出力
def print_horse_status(horses):
    print("\n---競走馬の情報---\n")
    for horse in horses:
        horse.print_horse_status()


if __name__ == "__main__":
    # テスト用url (2021年 日本ダービー)
    url = "https://race.netkeiba.com/race/shutuba.html?race_id=202105021211"

    # urlを入力
    url = input_race_url()
    # urlから　を取得
    soup = get_soup(url)

    # print_all_html(soup)
    # file_writer(soup, "html_prettify.txt")

    # 競走馬オブジェクトを生成
    horses = get_horse_status(soup)
    # 競走馬の情報を出力
    print_horse_status(horses)