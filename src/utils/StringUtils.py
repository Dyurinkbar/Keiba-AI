# 文字列の空白と改行コードをなくして返却
def replace_not_blank(str: str):
    return str.replace(" ", "").replace("\n", "")
