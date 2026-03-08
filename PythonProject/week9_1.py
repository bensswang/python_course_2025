number = int(input("Input : x ="))
number2 = abs(number) #轉換成正數
nnumber = str(number2) #轉換成字串
a = 0

for i in range(len(nnumber)):
    j = len(nnumber) -1 - i
    a = a + (number2//(10**j)) * (10**i) #取商數放到右邊依序往左放
    number2 = number2 % (10**(j)) #取餘數 把最高的一位數刪掉

if number >= 0:
    print("Output :", a)
else:
    a = -1 * a #負數需要成一個負號 因為是用絕對值後的數值做運算
    print("Output :", a)