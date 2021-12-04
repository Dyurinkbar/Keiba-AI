'''レース情報のオブジェクトクラス'''


class RaceResult:
    # 日付
    def set_date(self, date):
        self.date = date

    def get_date(self):
        return self.date

    # 開催場所
    def set_venue(self, venue):
        self.venue = venue

    def get_venue(self):
        return self.venue

    # 天気
    def set_weather(self, weather):
        self.weather = weather

    def get_weather(self):
        return self.weather

    # レース名
    def set_race_name(self, race_name):
        self.race_name = race_name

    def get_race_name(self):
        return self.race_name

    # 出馬頭数
    def set_horse_head_count(self, horse_head_count):
        self.horse_head_count = horse_head_count

    def get_horse_head_count(self):
        return self.horse_head_count

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

    # 着順
    def set_rank(self, rank):
        self.rank = rank

    def get_rank(self):
        return self.rank

    # 鞍上
    def set_jockey(self, jockey):
        self.jockey = jockey

    def get_jockey(self):
        return self.jockey

    # 斤量
    def set_penalty_weight(self, penalty_weight):
        self.penalty_weight = penalty_weight

    def get_penalty_weight(self):
        return self.penalty_weight

    # レースの距離
    def set_race_distance(self, distance):
        self.distance = distance

    def get_distance(self):
        return self.distance

    # 馬場状態
    def set_race_condition(self, race_condition):
        self.race_condition = race_condition

    def get_race_situation(self):
        return self.race_condition

    # タイム
    def set_time(self, time):
        self.time = time

    def get_time(self):
        return self.time

    # 着差
    def set_reach_difference(self, reach_difference):
        self.reach_difference = reach_difference

    def get_reach_difference(self):
        return self.reach_difference

    # 通過着順
    def set_passing_ranks(self, passing_ranks):
        self.passing_ranks = passing_ranks

    def get_passing_ranks(self):
        return self.passing_ranks

    # 上がりタイム
    def set_final_time(self, final_time):
        self.final_time = final_time

    def get_final_time(self):
        return self.final_time

    # 馬体重
    def set_body_weight(self, body_weight):
        self.body_weight = body_weight

    def get_body_weight(self):
        return self.body_weight

    # レース成績を表示
    def print_race_result_data(self):
        print("\n日付：" + self.date)
        print("開催場所：" + self.venue)
        print("天気：" + self.weather)
        print("レース名：" + self.race_name)
        print("出馬頭数：" + self.horse_head_count)
        print("枠：" + self.waku)
        print("馬番：" + self.umaban)
        print("着順：" + self.rank)
        print("鞍上：" + self.jockey)
        print("斤量：" + self.penalty_weight)
        print("距離：" + self.distance)
        print("馬場状態：" + self.race_condition)
        print("タイム：" + self.time)
        print("着差：" + self.reach_difference)
        print("通過着順：" + self.passing_ranks)
        print("上がりタイム：" + self.final_time)
        print("馬体重：" + self.body_weight)
        print("\n")


'''
	def set_(self,):
		self.  =
	def get_(self):
		return self.
'''
