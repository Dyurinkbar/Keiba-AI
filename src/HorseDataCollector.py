# 競走馬のデータを取得
import Race


# レース情報を取得
def get_horse_data_by_race(horse):
    for n in range(len(horse)):
        race = Race.Race()
