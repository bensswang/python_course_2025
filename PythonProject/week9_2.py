def judge(time):
    hr = time // 60 #分鐘取商數是小時
    mins = time % 60 #分鐘取餘數是分鐘
    miniszero = int(mins != 0) #如果分鐘不是0 miniszero會是1 要加20元
    money = hr * 40 + miniszero * 20
    if money > 300: #上限是300
        money = 300
    else:
        money = money
    return money, hr, mins

def main():
    time = int(input("停車時間(分鐘計費):"))
    money , hr, mins = judge(time)
    print(f"合計: {hr} 小時 {mins} 分\n應繳費用: {money}")

main()
