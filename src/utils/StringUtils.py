"""文字列の操作"""


# 文字列の空白と改行コードをなくして返却
def replace_shave_blank(word: str):
    return word.replace(" ", "").replace("　", "").replace("\n", "")


# 指定された文字をなくして返却
def replace_shave_designated(word: str, exclusion_words: str):
    for exclusion_word in exclusion_words:
        word = word.replace(exclusion_word, "")
    return word


# 年月日の漢字をスラッシュに置換して返却
# 同時にyyyy/mm/ddの形式に変換
def replace_date_to_slash(word: str):
    word = word.replace("年", "/").replace("月", "/").replace("日", "")
    # スラッシュで分割し、桁数を確認して0を挿入
    words = replace_shave_blank(word).split("/")
    word = ""
    for n in range(len(words)):
        # 年はそのまま、月と日が２文字じゃなければ、0挿入
        if n == 0 or len(words[n]) >= 2:
            word += words[n]
        else:
            word += "0" + words[n]
        # 最後以外にはスラッシュを戻す
        if n != len(words) - 1:
            word += "/"
    return word


# 文字列の空白と丸括弧をなくして返却
def replace_shave_parentheses(word: str):
    return replace_shave_blank(word).replace("(", "").replace(")", "")
