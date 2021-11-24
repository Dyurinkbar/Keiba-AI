# 文字列の空白と改行コードをなくして返却:引数(string)
def replace_not_blank(str):
    str.replace(" ", "").replace("\n", "")
    return str
