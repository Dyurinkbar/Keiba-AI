"""レース成績(DB)のオブジェクトクラス"""
import RaceDetail


class RaceResultDB:
    def __init__(self):
        self.rank = "?"
        self.waku = "?"
        self.umaban = "?"
        self.horse_name = "?"
        self.race_results_url = "?"
        self.seirei = "?"
        self.penalty_weight = "?"
        self.jockey = "?"
        self.time = "?"
        self.reach_difference = "?"
        self.passing_ranks = "?"
        self.odds = "?"
        self.favorite = "?"
        self.final_rap_time = "?"
        self.body_weight = "?"
        self.trainer_area = "?"
        self.owner = "?"

    # 着順
    def set_rank(self, rank):
        self.rank = rank

    def get_rank(self):
        return self.rank

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

    # 馬名
    def set_horse_name(self, horse_name):
        self.horse_name = horse_name

    def get_horse_name(self):
        return self.horse_name

    # 競走成績URL
    def set_race_results_url(self, race_results_url):
        self.race_results_url = race_results_url

    def get_race_results_url(self):
        return self.race_results_url

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

    # 鞍上
    def set_jockey(self, jockey):
        self.jockey = jockey

    def get_jockey(self):
        return self.jockey

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

    # オッズ
    def set_odds(self, odds):
        self.odds = odds

    def get_odds(self):
        return self.odds

    # 人気
    def set_favorite(self, favorite):
        self.favorite = favorite

    def get_favorite(self):
        return self.favorite

    # 上がりタイム
    def set_final_rap_time(self, final_rap_time):
        self.final_rap_time = final_rap_time

    def get_final_rap_time(self):
        return self.final_rap_time

    # 馬体重
    def set_body_weight(self, body_weight):
        self.body_weight = body_weight

    def get_body_weight(self):
        return self.body_weight

    # 厩舎地方
    def set_trainer_area(self, trainer_area):
        self.trainer_area = trainer_area

    def get_trainer_area(self):
        return self.trainer_area

    # 馬主
    def set_owner(self, owner):
        self.owner = owner

    def get_owner(self):
        return self.owner

    # レース成績を表示

    def print_race_result_data(self):
        print("着順　　：" + self.rank)
        print("枠　　　：" + self.waku)
        print("馬番　　：" + self.umaban)
        print("馬名　　：" + self.horse_name)
        print("競走成績URL：" + self.race_results_url)
        print("性齢　　：" + self.seirei)
        print("斤量　　：" + self.penalty_weight)
        print("鞍上　　：" + self.jockey)
        print("タイム　：" + self.time)
        print("着差　　：" + self.reach_difference)
        print("通過着順：" + self.passing_ranks)
        print("オッズ　：" + self.odds)
        print("人気　　：" + self.favorite)
        print("上がり　：" + self.final_rap_time)
        print("馬体重　：" + self.body_weight)
        print("厩舎地方：" + self.trainer_area)
        print("馬主　　：" + self.owner)
        print("\n")

    rank = property(get_rank, set_rank)
    waku = property(get_waku, set_waku)
    umaban = property(get_umaban, set_umaban)
    horse_name = property(get_horse_name, set_horse_name)
    race_results_url = property(get_race_results_url, set_race_results_url)
    seirei = property(get_seirei, set_seirei)
    penalty_weight = property(get_penalty_weight, set_penalty_weight)
    jockey = property(get_jockey, set_jockey)
    time = property(get_time, set_time)
    reach_difference = property(get_reach_difference, set_reach_difference)
    passing_ranks = property(get_passing_ranks, set_passing_ranks)
    odds = property(get_odds, set_odds())
    favorite = property(get_favorite, set_favorite)
    final_rap_time = property(get_final_rap_time, set_final_rap_time)
    body_weight = property(get_body_weight, set_body_weight)
    trainer_area = property(get_trainer_area, set_trainer_area)
    owner = property(get_owner, set_owner)
