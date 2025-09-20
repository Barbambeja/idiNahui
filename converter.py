a = input("Число: ")
a = int(a, int(input("Из: ")))
b = int(input("В: "))
out = "";
print()
while a != 0:
    print(a, "/", b, "=", a // b, "ост.", a % b)
    out = str(a % b) + out
    a = a // b
print(out)
