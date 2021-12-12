"""ファイル操作"""
import PathUtils


# 文字データをtxtに出力
def file_write_to_txt(content: str, file_name: str):
    try:
        with open(PathUtils.path_out + file_name +
                  ".txt", "w", encoding="UTF-8") as txt_file:
            txt_file.write(content)
            print("\n" + file_name + "を出力しました。\n")
    except:
        print("\n" + file_name + "の出力に失敗しました。\n")
