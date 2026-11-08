class SkibidiToilet:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def sl(self):
        rare = ""
        if 50 <= self.power <= 100:
            rare = "Ультра-мега-супер-хорош"
            return rare
        else:
            rare = "Попуск-отстой-ужас"
            return rare

    def __str__(self):
        return f"Твой скибиди туалет {self.name} имеет редкость {self.sl()}"

def filter(n):
    try:
        return int(n)
    except ValueError:
        return "Idiot I asked number"

def wow(n):
    if n == 67:
        print("This is not the place for such people")
        exit()
    else:
        print("good boy:)")

print("Hihahahaha")
num = input("Pls enter number for next actions:\n")
if filter(num):
    wow(int(num))

toilet = input("Введи имя твоего скибиди бойца:\n")
power_toilet = input("Введи силу твоего скибиди бойца:\n")
if filter(power_toilet):
    skibidi = SkibidiToilet(toilet, int(power_toilet))
    print(skibidi)