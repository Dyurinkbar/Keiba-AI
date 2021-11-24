# 馬の状態を保持するオブジェクト
class Horse:
    # def __init__(self):

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

    # 厩舎場所
    def set_trainer_place(self, trainer_place):
        self.trainer_place = trainer_place

    def get_trainer_place(self):
        return self.trainer_place

    # 競走成績URL
    def set_grade_url(self, grade_url):
        self.grade_url = grade_url

    def get_grade_url(self):
        return self.grade_url

    # 情報を出力
    def print_horse_status(self):
        print(self.waku + "枠 " + self.umaban +
              "番 " + self.name + " " + self.seirei + " 斤量" + self.penalty_weight + "kg " + self.trainer_place + " ")
        print(self.jockey + " 騎手" + "\n")