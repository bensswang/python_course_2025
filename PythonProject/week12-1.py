import ast
from collections import Counter

s = input("nums = ")
lst = ast.literal_eval(s) #可以辨識輸入的格式並轉換成不同格式 本題是轉換成list
count = Counter(lst)
print(Counter(lst).most_common()[0]) #輸出最多的單位、數量

