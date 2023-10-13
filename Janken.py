'''
Created on 2023/10/13

@author: t21cs058
'''
import random

def janken():
    # プレイヤーAとプレイヤーBの手をランダムに選択
    hand_a = random.randint(0, 2)
    hand_b = random.randint(0, 2)

    # じゃんけんの手の対応表
    hands = ["グー", "チョキ", "パー"]

    # 勝敗判定
    if hand_a == hand_b:
        result = "引き分け"
    elif (hand_a == 0 and hand_b == 1) or (hand_a == 1 and hand_b == 2) or (hand_a == 2 and hand_b == 0):
        result = "Aの勝ち"
    else:
        result = "Bの勝ち"

    # 結果を出力
    print(f"Aの手：{hands[hand_a]} v.s. Bの手：{hands[hand_b]} → {result}")

# ゲームを実行
janken()