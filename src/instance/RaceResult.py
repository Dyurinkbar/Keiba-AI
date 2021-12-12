"""レース成績のオブジェクトクラス"""


class RaceResult:
    def __init__(self):
        self.date = "?"
        self.venue = "?"
        self.weather = "?"
        self.race_name = "?"
        self.race_url = "?"
        self.horse_head_count = "?"
        self.waku = "?"
        self.umaban = "?"
        self.rank = "?"
        self.jockey = "?"
        self.penalty_weight = "?"
        self.distance = "?"
        self.race_condition = "?"
        self.time = "?"
        self.reach_difference = "?"
        self.passing_ranks = "?"
        self.pace = "?"
        self.final_rap_time = "?"
        self.body_weight = "?"

    # 日付

    @property
    def date(self):
        return self.date

    @date.setter
    def date(self, date):
        self.date = date

    # 開催場所

    @property
    def venue(self):
        return self.venue

    @venue.setter
    def venue(self, venue):
        self.venue = venue

    # 天気

    @property
    def weather(self):
        return self.weather

    @weather.setter
    def weather(self, weather):
        self.weather = weather

    # レース名

    @property
    def race_name(self):
        return self.race_name

    @race_name.setter
    def race_name(self, race_name):
        self.race_name = race_name

    # レース名

    @property
    def race_url(self):
        return self.race_url

    @race_url.setter
    def race_url(self, race_url):
        self.race_url = race_url

    # 出馬頭数

    @property
    def horse_head_count(self):
        return self.horse_head_count

    @horse_head_count.setter
    def horse_head_count(self, horse_head_count):
        self.horse_head_count = horse_head_count

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

    # 着順

    @property
    def rank(self):
        return self.rank

    @rank.setter
    def rank(self, rank):
        self.rank = rank

    # 鞍上

    @property
    def jockey(self):
        return self.jockey

    @jockey.setter
    def jockey(self, jockey):
        self.jockey = jockey

    # 斤量

    @property
    def penalty_weight(self):
        return self.penalty_weight

    @penalty_weight.setter
    def penalty_weight(self, penalty_weight):
        self.penalty_weight = penalty_weight

    # レースの距離

    @property
    def race_distance(self):
        return self.distance

    @race_distance.setter
    def race_distance(self, distance):
        self.distance = distance

    # 馬場状態

    @property
    def race_condition(self):
        return self.race_condition

    @race_condition.setter
    def race_condition(self, race_condition):
        self.race_condition = race_condition

    # タイム

    @property
    def time(self):
        return self.time

    @time.setter
    def time(self, time):
        self.time = time

    # 着差

    @property
    def reach_difference(self):
        return self.reach_difference

    @reach_difference.setter
    def reach_difference(self, reach_difference):
        self.reach_difference = reach_difference

    # 通過着順

    @property
    def passing_ranks(self):
        return self.passing_ranks

    @passing_ranks.setter
    def passing_ranks(self, passing_ranks):
        self.passing_ranks = passing_ranks

    # ペース

    @property
    def pace(self):
        return self.pace

    @pace.setter
    def pace(self, pace):
        self.pace = pace

    # 上がりタイム

    @property
    def final_rap_time(self):
        return self.final_rap_time

    @final_rap_time.setter
    def final_rap_time(self, final_rap_time):
        self.final_rap_time = final_rap_time

    # 馬体重

    @property
    def body_weight(self):
        return self.body_weight

    @body_weight.setter
    def body_weight(self, body_weight):
        self.body_weight = body_weight

    # レース成績を表示
    def print_race_result_data(self):
        print("\n日付　　：" + self.date)
        print("開催場所：" + self.venue)
        print("天気　　：" + self.weather)
        print("レース名：" + self.race_name)
        print("レースURL：" + self.race_url)
        print("出馬頭数：" + self.horse_head_count)
        print("枠　　　：" + self.waku)
        print("馬番　　：" + self.umaban)
        print("着順　　：" + self.rank)
        print("鞍上　　：" + self.jockey)
        print("斤量　　：" + self.penalty_weight)
        print("距離　　：" + self.distance)
        print("馬場状態：" + self.race_condition)
        print("タイム　：" + self.time)
        print("着差　　：" + self.reach_difference)
        print("通過着順：" + self.passing_ranks)
        print("ペース　：" + self.pace)
        print("上がり　：" + self.final_rap_time)
        print("馬体重　：" + self.body_weight)
        print("\n")


'''
    def set_(self,):
        self.  =
        def get_(self):
            return self.
'''
