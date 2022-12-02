import pandas as pd
import random
random.seed(0)

# 売上データを生成
def uriage():
    df = pd.DataFrame({
        'No' : range(1, 1001),
        '売上日' : random.choices(pd.date_range(start='2022/1/1', freq='d', periods=10), k=1000),
        '担当者' : random.choices('織田信長 豊臣秀吉 徳川家康 毛利元就 北条氏康 武田信玄 上杉謙信 島津義弘 立花宗茂'.split(), k=1000),
        '商品' : random.choices('卵 牛乳 砂糖 小麦粉 バター チョコレート チーズ イチゴ'.split(), k=1000),
        '単価' : random.choices(range(100, 501), k=1000),
        '数量' : random.choices(range(1,11), k=1000)
    })

    # 担当者をリストで取得
    tantou_list = ["本多灯","瀬戸大也","森本哲平","阪本祐也","田中大貴"]#df['担当者'].unique().tolist()

    return df, tantou_list
