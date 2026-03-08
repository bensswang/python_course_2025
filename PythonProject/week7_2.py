def calculate_bmi(weight, height):
    bmi =  weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    result = ""
    if bmi < 18.5:
        result = "體重過輕"
    elif bmi < 24:
        result = "正常"
    elif bmi < 30:
        result = "過重"
    else:
        result = "肥胖"
    return result

def main():
    height = float(input("請輸入身高(公尺) :"))
    weight = float(input("請輸入體重(公斤) :"))
    bmi = calculate_bmi(weight, height)
    result = classify_bmi(bmi)
    print("你的BMI為 :", round(bmi, 2))
    print("體重分類 :", result)

main()
