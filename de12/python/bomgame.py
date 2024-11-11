import random
choices =["赤色","青色","黄色"]

correct_choices = random.choices

print("爆弾を止めよう！")
print("次の中からコードの色を選ぼう:赤色 ,1:青色 ,2:黄色")

while True:
    guess = input ("あなたの選択した色")
        if guess == correct_choices:
            print("死亡です！　ゲームオーバー")
            break
            
        else :
            print("生存しました！ あと1本！　確率は２分の１　\n")
        

        
        