grades = {} #建立空的dictionary
sum = 0
while True:
    name = str(input("Enter student name (or 'end' to stop):"))
    if name == "end": #輸入end結束程式
        break
    else:
        grades[name] = int(input("Enter score:")) #名字對應到輸入的成績

print("=== 成績列表 ===")
for key in grades:
    print(f"{key}: {grades[key]}") #一組一組的輸出
for key in grades:
    sum += grades[key] #每一項對應到的成績加總
avr = sum / len(grades) #成績總和/學生人數(字典長度)
print(f"平均分數:{avr}")
if avr >= 60: #>= 60及格
    print("全班平均及格")
else: #<60不及格
    print("全班平均不及格")

