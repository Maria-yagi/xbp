import random
choices =["赤色","青色","黄色"]

print("爆弾を止めよう！")
print("0:赤色 ,1:青色 ,2:黄色")

while True:
        user_choice =int("あなたの運命を決めましょう！（0,1,2):")
        computer_choice=random.randint(0,2)
        print(f"あなた:{choices[user_choice]},  ボンバーマン: {choices[computer_choice]}")

        if user_choice==computer_choice:
            print("死亡　残念")
        elif (user_choice ==0 and computer_choice==1)
             (user_choice ==0 and computer_choice==2)
             (user_choice ==1 and computer_choice==0)
             (user_choice ==1 and computer_choice==2)
             (user_choice ==2 and computer_choice)