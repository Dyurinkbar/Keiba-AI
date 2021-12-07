'''データを処理するためのデータを取得'''
from bs4 import BeautifulSoup as bs

import utils.SoupUtils as SoupUtils


# 重賞一覧ページからレース名を取得
# 過去のレース名を参照する際に使用
def print_graded_race_name():
    # URLからHTMLを取得
    soup = SoupUtils.get_soup("https://race.netkeiba.com/top/schedule.html")

    # レース名を取得
    graded_race_names = soup.select("td[class^=Race_Name] > a")

    # レース名を表示
    [print(graded_race_name.text) for graded_race_name in graded_race_names]


if __name__ == "__main__":
    # 欲しいデータを取得できるメソッドを起動
    print_graded_race_name()
