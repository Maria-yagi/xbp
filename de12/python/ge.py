
import random

def janken_game():
    # 手の選択肢
    choices = ["グー", "チョキ", "パー"]
    
    # プレイヤーの入力
    print("じゃんけんゲームへようこそ！")
    player_choice = input("あなたの手を選んでください (グー/チョキ/パー): ")
    
    # 入力が正しいか確認
    if player_choice not in choices:
        print("無効な入力です。グー、チョキ、またはパーを入力してください。")
        return
    
    # コンピュータの手をランダムに選ぶ
    computer_choice = random.choice(choices)
    
    print(f"コンピュータの手: {computer_choice}")
    print(f"あなたの手: {player_choice}")
    
    # 勝敗を判定
    if player_choice == computer_choice:
        print("引き分けです！")
    elif (player_choice == "グー" and computer_choice == "チョキ") or \
         (player_choice == "チョキ" and computer_choice == "パー") or \
         (player_choice == "パー" and computer_choice == "グー"):
        print("あなたの勝ちです！")
    else:
        print("コンピュータの勝ちです！")

# ゲームを開始
janken_game()
