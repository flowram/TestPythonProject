class SkibidiToilet:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def sl(self):
        rare = ""
        if 50 <= power <= 100:
            rare = "Ультра-мега-супер-хорош"
            return rare
        else:
            rare = "Попуск-отстой-ужас"
            return rare

    def __str__(self):
        return f"Твой скибиди туалет {self.name} имеет редкость {self.sl()}"


def wow(n):
    if n == 67:
        print("go out:(")
    else:
        print("good boy:)")

print("Hihahahaha")
try:
    num = int(input("Pls enter number:\n"))
except ValueError:
    print("Idiot I asked number")
else:
    wow(num)