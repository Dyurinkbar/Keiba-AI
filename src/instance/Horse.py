"""馬の状態を保持するオブジェクト"""
import RaceResult
import RaceDetail


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
    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

    # 鞍上
    @property
    def jockey(self):
        return self.jockey

    @jockey.setter
    def jockey(self, jockey):
        self.jockey = jockey

    # 枠

    @property
    def waku(self):
        return self.waku

    @waku.setter
    def waku(self, waku):
        self.waku = waku

    # 馬番

    @property
    def umaban(self):
        return self.umaban

    @umaban.setter
    def umaban(self, umaban):
        self.umaban = umaban

    # 性齢

    @property
    def seirei(self):
        return self.seirei

    @seirei.setter
    def seirei(self, seirei):
        self.seirei = seirei

    # 斤量

    @property
    def penalty_weight(self):
        return self.penalty_weight

    @penalty_weight.setter
    def penalty_weight(self, penalty_weight):
        self.penalty_weight = penalty_weight

    # 厩舎地方

    @property
    def trainer_area(self):
        return self.trainer_area

    @trainer_area.setter
    def trainer_area(self, trainer_area):
        self.trainer_area = trainer_area

    # 競走成績URL

    @property
    def race_results_url(self):
        return self.race_results_url

    @race_results_url.setter
    def race_results_url(self, race_results_url):
        self.race_results_url = race_results_url

    # 調教師

    @property
    def trainer(self):
        return self.trainer

    @trainer.setter
    def trainer(self, trainer):
        self.trainer = trainer

    # 馬主

    @property
    def owner(self):
        return self.owner

    @owner.setter
    def owner(self, owner):
        self.owner = owner

    # 生産者
    @property
    def breeder(self):
        return self.breeder

    @breeder.setter
    def breeder(self, breeder):
        self.breeder = breeder

    # 生年月日

    @property
    def birthday(self):
        return self.birthday

    @birthday.setter
    def birthday(self, birthday):
        self.birthday = birthday

    # 血統

    @property
    def edigrees(self):
        return self.edigrees

    @edigrees.setter
    def edigrees(self, edigrees):
        self.edigrees = edigrees

    # 競走成績オブジェクト

    @property
    def race_results(self):
        return self.race_results

    @race_results.setter
    def race_results(self, race_results: RaceResult):
        self.race_results = race_results

    def add_race_results(self, race_result: RaceResult):
        self.race_results.append(race_result)

    # 情報を出力
    def print_horse_data(self):
        print(self.waku + "枠 " + self.umaban +
              "番 " + self.name + " " + self.seirei + " 斤量" + self.penalty_weight + "kg " + self.trainer_area + " ")
        print(self.jockey + " 騎手")
        print(self.birthday + " 生まれ")
        print("調教師：" + self.trainer)
        print("馬主　：" + self.owner)
        print("生産者：" + self.breeder)
        print("母　：" + self.edigrees["母"])
        print("父　：" + self.edigrees["父"])
        print("父母：" + self.edigrees["父母"])
        print("父父：" + self.edigrees["父父"])
        print("母父：" + self.edigrees["母父"])
        print("母母：" + self.edigrees["母母"])
        print("\n")
