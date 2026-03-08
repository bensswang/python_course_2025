items = ["apple", "banana", "milk", "bread", "cheese"] #一個儲存商品的Llist
list =  [] #購物車的list

while True:
    print("""--- Shopping Cart ---
1. 查看商品列表
2. 加入商品到購物車
3. 移除購物車商品
4. 查看購物車內容
5. 結帳（結束程式）
請輸入選項（1-5）：""")
    num = int(input(""))
    if num == 1: #輸入1列印商品種類
        print("可購買的商品如下：")
        for i in range(1, len(items)+1): #依次從商品的list列出物品
            print(f"{i}. {items[i-1]}")

    elif num == 2: #輸入2加入購物車
        add = str(input("請輸入要加入的商品名稱：")) #輸入轉為字串
        if add in items: #如果輸入的字串在物品的清單內
            list.append(add) #加到購物車
            print(f"\n已從購物車加入{add}\n")
        else: #否則不存在
            print("\n商品不存在，無法加入。\n")

    elif num == 3: #輸入3移除商品
        rem = str(input("請輸入要移除的商品名稱：")) #輸入轉為字串
        if list == []: #購物車沒有東西
            print("\n購物車目前是空的，無法移除商品。\n")
        elif rem in list: #要移除的商品在購物車內
            list.remove(rem)
            print(f"\n已從購物車移除{rem}\n")
        else: # #要移除的商品不在購物車內
            print("\n購物車中沒有此商品。\n")

    elif num == 4: #輸入4顯示購物車的東西
        if list == []: #購物車沒有東西
            print("\n購物車是空的\n")
        else: #否則輸出購物車的內容
            print("你的購物車內容:")
            for j in range(0, len(list)): #依次從購物車的list列出物品
                print(list[j])

    elif num == 5: #輸入5結帳
        print("你購買了以下商品:")
        for l in range(0, len(list)):  #依次從購物車的list列出物品
            print(list[l])
        print("感謝使用，結帳完成!")
        break #結束程式








