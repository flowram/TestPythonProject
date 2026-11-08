
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