ori = input()
orii = ori.split()

while True:
    e = input()
    ee = e.split()
    cmd = ee[0]
    idx = int(ee[1])
    val = ee[1]  # 字串形式

    if cmd == "a":
        orii.append(val)

    elif cmd == "r":
        if val in orii:
            orii.remove(val)

    elif cmd == "p":
        if 0 <= idx < len(orii):
            orii.pop(idx)

    elif cmd == "q":
        if not (0 <= idx < len(orii)):
            print("Error")
            break
        else:
            print(orii[idx])
            total = sum(map(int, orii))
            print(total // len(orii))
            break