'''データを整理'''
import instance.Horse as Horse


# 競走馬の情報からデータを整理
def horses_data_organize(horses: Horse):
    # 競走馬を順番に情報整理
    for horse in horses:
        print(f'{horse.get_name()}のデータを整理します。')

    return horses
