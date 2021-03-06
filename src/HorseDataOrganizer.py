"""データを整理"""
import instance.Horse as Horse
import instance.RaceDetail as RaceDetail


# 競走馬の情報からデータを整理
def horses_data_organize(horses: Horse, race_detail: RaceDetail):
    print("\n競走馬の情報を整理します。")
    # 競走馬を順番に情報整理
    for horse in horses:
        print(f'{horse.get_name()}のデータを整理します。')

    print("整理が終わりました。\n")
    return horses
