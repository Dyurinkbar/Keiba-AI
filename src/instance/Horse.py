'''馬の状態を保持するオブジェクト'''
from instance.RaceResult import RaceResult
from instance.RaceDetail import RaceDetail


class Horse:
    # コンストラクタ(空値が好ましくないので、空文字を代入)
    def __init__(self):
        self.name = "?"
        self.jockey = "?"
        self.waku = "?"
        self.umaban = "?"
        self.seirei = "?"
        self.penalty_weight = "?"
        self.trainer = "?"
        self.race_results_url = "?"
        self.trainer = "?"
        self.owner = "?"
        self.breeder = "?"
        self.birthday = "?"

    # 馬名
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    # 鞍上
    def set_jockey(self, jockey):
        self.jockey = jockey

    def get_jockey(self):
        return self.jockey

    # 枠
    def set_waku(self, waku):
        self.waku = waku

    def get_waku(self):
        return self.waku

    # 馬番
    def set_umaban(self, umaban):
        self.umaban = umaban

    def get_umaban(self):
        return self.umaban

    # 性齢
    def set_seirei(self, seirei):
        self.seirei = seirei

    def get_seirei(self):
        return self.seirei

    # 斤量
    def set_penalty_weight(self, penalty_weight):
        self.penalty_weight = penalty_weight

    def get_penalty_weight(self):
        return self.penalty_weight

    # 厩舎地方
    def set_trainer_area(self, trainer_area):
        self.trainer_area = trainer_area

    def get_trainer_area(self):
        return self.trainer_area

    # 競走成績URL
    def set_race_results_url(self, race_results_url):
        self.race_results_url = race_results_url

    def get_race_results_url(self):
        return self.race_results_url

    # 調教師
    def set_trainer(self, trainer):
        self.trainer = trainer

    def get_trainer(self):
        return self.trainer

    # 馬主
    def set_owner(self, owner):
        self.owner = owner

    def get_owner(self):
        return self.owner

    # 生産者
    def set_breeder(self, breeder):
        self.breeder = breeder

    def get_breeder(self):
        return self.breeder

    # 生年月日
    def set_birthday(self, birthday):
        self.birthday = birthday

    def get_birthday(self):
        return self.birthday

    # 血統
    def set_edigrees(self, edigrees):
        self.edigrees = edigrees

    def get_edigrees(self):
        return self.edigrees

    # 競走成績オブジェクト
    def set_race_results(self, race_results: RaceResult):
        self.race_results = race_results

    def get_race_results(self):
        return self.race_results

    def add_race_results(self, race_result: RaceResult):
        self.race_results.append(race_result)

    # 情報を出力
    def print_horse_data(self):
        print(self.name + "\n")
        print("枠　　　：" + self.waku)
        print("番　　　：" + self.umaban)
        print("性齢　　：" + self.seirei)
        print("斤量　　：" + self.penalty_weight)
        print("厩舎地方：" + self.trainer_area)
        print("騎手　　：" + self.jockey)
        print("誕生日　：" + self.birthday)
        print("調教師　：" + self.trainer)
        print("馬主　　：" + self.owner)
        print("生産者　：" + self.breeder)
        print("母　：" + self.edigrees["母"])
        print("父　：" + self.edigrees["父"])
        print("父母：" + self.edigrees["父母"])
        print("父父：" + self.edigrees["父父"])
        print("母父：" + self.edigrees["母父"])
        print("母母：" + self.edigrees["母母"])
        print("\n")
