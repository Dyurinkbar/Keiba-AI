'''分析対象のレース情報オブジェクト'''


class RaceDetail():
    # レース名
    def set_race_name(self, race_name):
        self.race_name = race_name

    def get_race_name(self):
        return self.race_name

    # 距離と馬場
    def set_distance_and_racetrack(self, distance_and_racetrack):
        self.distance_and_racetrack = distance_and_racetrack

    def get_distance_and_racetrack(self):
        return self.distance_and_racetrack

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


'''
	def set_(self,):
		self.  =
	def get_(self):
		return self.
'''
