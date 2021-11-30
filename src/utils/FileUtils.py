# ファイル操作
import utils.PathUtils as PathUtils


# 文字データをtxtに出力
def file_write_to_txt(content, file_name):
    txt_file = open(PathUtils.path_out + file_name +
                    ".txt", "w", encoding="UTF-8")
    txt_file.write(content)
    txt_file.close()
    print("\n" + file_name + "を出力しました。\n")
