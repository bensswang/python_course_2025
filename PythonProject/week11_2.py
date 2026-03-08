ori = input()
orii = ori.split()
all = 0

while 1:
    e = input()
    ee = e.split()
    pee = ee[0]
    iee = int(ee[1])
    see = str(ee[1])
    if pee == "q":
        # print(orii, iee)
        if not (0 <= iee < len(orii)):
            print("Error")
            break
        else:
            print(orii[iee])
            for i in orii:
                i = int(i)
                all = all + i
            print(int(all/(len(orii))))
            # print(orii)
            break
    elif pee == "a":
        orii.append(see)
        # print(orii)
    elif pee == "r":
        if see in orii:
            orii.remove(see)
        # print(orii)
    elif pee == "p":
        if see in orii:
            orii.pop(iee)
        # print(orii)
    # elif pee == "q":
    #     if len(orii) < iee:
    #         print("Error")
    #         # print(orii)
    #         break
    #     else:
    #         print(orii[iee])
    #         for i in orii:
    #             i = int(i)
    #             all = all + i
    #         print(int(all/(len(orii))))
    #         # print(orii)
    #         break










