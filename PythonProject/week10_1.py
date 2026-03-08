import random
from random import randint

ans = (random.randint(0, 99))#取一個0~99之間的整數
#print(ans)
count = 10 #計數器設定十次
while True:
    guess = int(input("請猜數字(0~99):"))
    if guess == ans: #猜對
        print("BINGO!")
        break
    elif guess < ans: #猜太小
        print(f"ans > {guess}")
        count = count - 1
        #print(count)
    elif guess > ans: #猜太大
        print(f"ans < {guess}")
        count = count - 1
        #print(count)
    if count == 0:  #當計數器歸零 輸出挑戰失敗
        print(f"猜 10 次了！你輸了！\n正確答案是： {ans}")
        break
