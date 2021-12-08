'''分析対象のレース情報オブジェクト'''


class RaceDetail():
    # コンストラクタ(空値が好ましくないので、空文字を代入)
    def __init__(self):
        self.race_name = "データなし"
        self.race_url = "データなし"
        self.distance_and_racetrack = "データなし"
        self.around = "データなし"
        self.weather = "データなし"
        self.race_condition = "データなし"
        self.venue = "データなし"
        self.entry_terms = "データなし"
        self.grade = "データなし"
        self.penalty_weight_setting = "データなし"
        self.horse_head_count = "データなし"

    # レース名
    def set_race_name(self, race_name):
        self.race_name = race_name

    def get_race_name(self):
        return self.race_name

    # レースURL
    def set_race_url(self, race_url):
        self.race_url = race_url

    def get_race_url(self):
        return self.race_url

    # 距離と馬場
    def set_distance_and_racetrack(self, distance_and_racetrack):
        self.distance_and_racetrack = distance_and_racetrack

    def get_distance_and_racetrack(self):
        return self.distance_and_racetrack

    # 内外回り
    def set_around(self, around):
        self.around = around

    def get_around(self):
        return self.around

    # 天候
    def set_weather(self, weather):
        self.weather = weather

    def get_weather(self):
        return self.weather

    # 馬場状態
    def set_race_condition(self, race_condition):
        self.race_condition = race_condition

    def get_race_condition(self):
        return self.race_condition

    # 開催場所
    def set_venue(self, venue):
        self.venue = venue

    def get_venue(self):
        return self.venue

    # 出馬条件
    def set_entry_terms(self, entry_terms):
        self.entry_terms = entry_terms

    def get_entry_terms(self):
        return self.entry_terms

    # クラス
    def set_grade(self, grade):
        self.grade = grade

    def get_grade(self):
        return self.grade

    # 斤量設定
    def set_penalty_weight_setting(self, penalty_weight_setting):
        self.penalty_weight_setting = penalty_weight_setting

    def get_penalty_weight_setting(self):
        return self.penalty_weight_setting

    # 出馬頭数
    def set_horse_head_count(self, horse_head_count):
        self.horse_head_count = horse_head_count

    def get_horse_head_count(self):
        return self.horse_head_count

    # レース情報を表示
    def print_race_detail(self):
        print(f"レース名：{self.race_name}")
        print(f"レースURL：{self.race_url}")
        print(f"距離と馬場：{self.distance_and_racetrack}")
        print(f"内外回り：{self.around}")
        print(f"天候：{self.weather}")
        print(f"馬場状態：{self.race_condition}")
        print(f"開催場所：{self.venue}")
        print(f"出馬条件：{self.entry_terms}")
        print(f"クラス：{self.grade}")
        print(f"斤量設定：{self.penalty_weight_setting}")
        print(f"出馬頭数：{self.horse_head_count}")
        print()
