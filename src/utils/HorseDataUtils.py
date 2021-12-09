'''競走馬のデータを使いやすくする'''


# レースの開催場所から、右回りか左回り(右、左)を返却
def get_around_from_venue(venue: str):
    around = ""
    # 開催場所と周回方向のMap
    venue_dict = {"東京": "左", "中京": "左", "新潟": "左", "中山": "右",
                  "阪神": "右", "京都": "右", "札幌": "右", "函館": "右", "福島": "右", "小倉": "右"}
    # 開催場所によって、周回方向を取得
    try:
        around = venue_dict[venue]
    except:
        print("開催場所が一致しませんでした。")
        around = "不明"
    return around

# レース名を出馬表→DB表記に変更
