in_list = input().split()
while True:
    cmd = input().split()
    if cmd[0] == "q":
        if int(cmd[1]) >= len(in_list):
            print("Error")
        else:
            print(in_list[int(cmd[1])])
            print(int(sum(int(x) for x in in_list)/len(in_list)))
        break
    elif cmd[0] == "a":
        in_list.append(cmd[1])
    elif cmd[0] == "r":
        if cmd[1] in in_list:
            in_list.remove(cmd[1])
    elif cmd[0] == "p":
        if int(cmd[1]) < len(in_list):
            in_list.pop(int(cmd[1]))