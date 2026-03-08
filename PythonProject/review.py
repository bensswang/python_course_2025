class man:
    def __init__(self, name, height, weight, length, age):
        self.name = name
        self.height = height
        self.weight = weight
        self.length = length
        self.age = age

    def drialc(self):
        if self.age < 18:
            yn = "n"
        else:
            yn = "y"
        return yn

class boy(man):
    def __init__(self, name, height, weight, length, age):
        self.name = name
        self.height = height
        self.weight = weight
        self.length = length
        self.age = 6
    def cheat(self, ask):
        if ask == "n":
            ch = "none"
        elif self.age < 10:
            ch = "no"
        else:
            ch = "yes"
        return ch



wang = man("ss", 180, 65, 30, 19)
chang = boy("shaote", 160, 70, 12, 16)
print(wang.name)
print(chang.age)
print(f"drink? {wang.drialc()}")
print(f"drink? {chang.drialc()}")
#print(f"cheat? {wang.cheat("n")}")
print(f"cheat? {chang.cheat("n")}")

