#一対一のじゃんけんをシュミレートする
import random

#Aがどの手を出したかを標準出力する
def Jyanken_A_Hand_Print(a):
    if a == 0:
        print('Aの手：グー v.s. ', end="")
    elif a == 1:
        print('Aの手：チョキ v.s. ', end="")
    elif a == 2:
        print('Aの手：パー v.s. ', end="")
        
#Bがどの手を出したかを標準出力する       
def Jyanken_B_Hand_Print(b):
    if b == 0:
        print('Bの手：グー -> ', end="")
    elif b == 1:
        print('Bの手：チョキ -> ', end="")
    elif b == 2:
        print('Bの手：パー -> ', end="")
        
#じゃんけんの勝敗判定を行う関数
def Jyanken_Judge(a,b):
    if a == b:
        print('引き分け') 
    elif a == 0 and b == 1:
        print('Aの勝ち')
    elif a == 0 and b == 2:
        print('Aの負け')
    elif a == 1 and b == 0:
        print('Aの負け')
    elif a == 1 and b == 2:
        print('Aの勝ち')
    elif a == 2 and b == 0:
        print('Aの勝ち')
    elif a == 2 and b == 1:
        print('Aの負け')
        
#出す手をランダムに決める
a = random.randint(0,2)
b = random.randint(0,2)

#出す手を標準出力
Jyanken_A_Hand_Print(a)
Jyanken_B_Hand_Print(b)

#じゃんけんの勝敗を標準出力
Jyanken_Judge(a,b)





    
