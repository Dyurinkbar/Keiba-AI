'''データを表示する'''
from instance.Horse import Horse
from instance.RaceDetail import RaceDetail
from instance.RaceResult import RaceResult
from instance.RaceResultDB import RaceResultDB


# 競走馬の情報を出力(リスト)
def print_horses_data(horses: Horse):
    print("\n---競走馬の情報---\n")
    for horse in horses:
        print_horse_data(horse)


# 競走馬の情報を出力
def print_horse_data(horse: Horse):
    horse.print_horse_data()


# 競走馬のレース成績を表示(リスト)
def print_races_results(horses: Horse):
    print("\n---レースの戦績---\n")
    for horse in horses:
        print_race_results(horse)


# 競走馬のレース成績を表示
def print_race_results(horse: Horse):
    print(horse.get_name())
    race_results = horse.get_race_results()
    for race_result in race_results:
        race_result.print_race_result_data()


# 競走馬の情報を出力
def print_race_detail(race_detail: RaceDetail):
    print("\n---レースの情報---\n")
    race_detail.print_race_detail()


# レースのDBの情報を表示
def print_race_results_db(race_results_db: RaceResultDB):
    print("\n---レースDBの情報---\n")
    for race_result_db in race_results_db:
        race_result_db.print_race_result_data()
