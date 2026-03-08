import ast

s = input("nums1 = ")
p = input("nums2 = ")
fin = []
lst1 = ast.literal_eval(s)
lst2 = ast.literal_eval(p) #像上一個題目 轉換成list
set1 = set(lst1)
set2 = set(lst2) #分別轉換成集合
for i in set1:
    if i in set2: #如果在第一個集合裡面的元素也在第二個裡面
        n = min(lst1.count(i), lst2.count(i)) #取list中那個元素的數量 並取較小的那個
        fin += [i] * n #元素乘以共有的最小數量 加到list中

print(fin)


