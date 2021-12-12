"""分析対象のレース情報オブジェクト"""


class RaceDetail:
    # コンストラクタ(空値が好ましくないので、空文字を代入)
    def __init__(self):
        self.race_name = "?"
        self.race_url = "?"
        self.distance_and_racetrack = "?"
        self.around = "?"
        self.weather = "?"
        self.race_condition = "?"
        self.venue = "?"
        self.date = "?"
        self.entry_terms = "?"
        self.grade = "?"
        self.penalty_weight_setting = "?"
        self.horse_head_count = "?"

    # レース名
    @property
    def race_name(self):
        return self.race_name

    @race_name.setter
    def race_name(self, race_name):
        self.race_name = race_name

    # レースURL

    @property
    def race_url(self):
        return self.race_url

    @race_url.setter
    def race_url(self, race_url):
        self.race_url = race_url

    # 距離と馬場

    @property
    def distance_and_racetrack(self):
        return self.distance_and_racetrack

    @distance_and_racetrack.setter
    def distance_and_racetrack(self, distance_and_racetrack):
        self.distance_and_racetrack = distance_and_racetrack

    # 周回方向

    @property
    def around(self):
        return self.around

    @around.setter
    def around(self, around):
        self.around = around

    # 天候

    @property
    def weather(self):
        return self.weather

    @weather.setter
    def weather(self, weather):
        self.weather = weather

    # 馬場状態

    @property
    def race_condition(self):
        return self.race_condition

    @race_condition.setter
    def race_condition(self, race_condition):
        self.race_condition = race_condition

    # 開催場所

    @property
    def venue(self):
        return self.venue

    @venue.setter
    def venue(self, venue):
        self.venue = venue

    # 開催日

    @property
    def date(self):
        return self.date

    @date.setter
    def date(self, date):
        self.date = date

    # 出馬条件

    @property
    def entry_terms(self):
        return self.entry_terms

    @entry_terms.setter
    def entry_terms(self, entry_terms):
        self.entry_terms = entry_terms

    # クラス

    @property
    def grade(self):
        return self.grade

    @grade.setter
    def grade(self, grade):
        self.grade = grade

    # 斤量設定

    @property
    def penalty_weight_setting(self):
        return self.penalty_weight_setting

    @penalty_weight_setting.setter
    def penalty_weight_setting(self, penalty_weight_setting):
        self.penalty_weight_setting = penalty_weight_setting

    # 出馬頭数

    @property
    def horse_head_count(self):
        return self.horse_head_count

    @horse_head_count.setter
    def horse_head_count(self, horse_head_count):
        self.horse_head_count = horse_head_count

    # レース情報を表示
    def print_race_detail(self):
        print(f"レース名　：{self.race_name}")
        print(f"レースURL ：{self.race_url}")
        print(f"距離と馬場：{self.distance_and_racetrack}")
        print(f"周回方向　：{self.around}")
        print(f"天候　　　：{self.weather}")
        print(f"馬場状態　：{self.race_condition}")
        print(f"開催場所　：{self.venue}")
        print(f"開催日　　：{self.date}")
        print(f"出馬条件　：{self.entry_terms}")
        print(f"クラス　　：{self.grade}")
        print(f"斤量設定　：{self.penalty_weight_setting}")
        print(f"出馬頭数　：{self.horse_head_count}")
        print("\n")
