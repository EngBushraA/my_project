# calc_buggy.py

def c(a, b, o):
    if o == "+":
        return a + b
    if o == "-":
        return a - b
    if o == "*":
        return a * b
    if o == "/":
        if b == 0:
            print("no")
            return
        return a / b

print("WLCM")
x = int(input("num1: "))
y = int(input("num2: "))
z = input("op: ")

print("ans: ", c(x, y, z))

