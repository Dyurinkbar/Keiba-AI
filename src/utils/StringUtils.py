'''文字列の操作'''


# 文字列の空白と改行コードをなくして返却
def replace_not_blank(str: str):
    return str.replace(" ", "").replace("　", "").replace("\n", "")


# 文字列の空白と丸括弧をなくして返却
def replace_not_parentheses(str: str):
    return replace_not_blank(str).replace("(", "").replace(")", "")
