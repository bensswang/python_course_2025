# 向量格式: [age, gender(0女1男), seniority, 親等(0, 1, 2...)]
roles = {
    "我":   [2, 0, 0],   # ← 修正成 3 個值（seniority 你先設 0）
    "妻子": [0, 0, 0],
    "哥哥": [1, 1, 0],
    "姊姊": [1, 0, 0],
    "弟弟": [-1, 1, 0],
    "妹妹": [-1, 0, 0],
    "兄弟": [0, 1, 0],
    "姊妹": [0, 0, 0],
    "爸爸": [1, 1, 1],
    "媽媽": [1, 0, 1],
    "兒子": [-1, 1, -1],
    "女兒": [-1, 0, -1],
}


reverse = {}
for k, v in roles.items():
    t = tuple(v)
    if t in reverse:
        reverse[t] = None
    else:
        reverse[t] = k

inn = input('輸入關係，並以"我的"開頭: ').strip()
parts = inn.split("的")[1:]

relation = []
for p in parts:
    if p in roles:
        relation.append(roles[p])
    else:
        print(f"找不到關係字：{p}")

#print("relation =", relation)


# age: 累加（你原本的做法）
age = sum(v[0] for v in relation) if relation else 0

# gender: 用最後一個人的 gender（你原本其實就是在做「最後一個覆蓋」）
gender = relation[-1][1] if relation else 0

# seniority: 累加（你原本的做法）
seniority = sum(v[2] for v in relation) if relation else 0

relation2 = [age, gender, seniority]
#print("relation2 =", relation2)

# ---- 反查名稱 ----
name = reverse.get(tuple(relation2), None)
if name is None:
    print("這個向量找不到唯一名稱（可能不存在或不唯一）")
else:
    print(name)
