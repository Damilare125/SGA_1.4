# if statement practice
x = int(input("Please input your grade:"))
if type (x) == int:
    x = int(x)
    if x >= 70:
        print("A")
    elif x >= 60 and x <= 69:
        print("B")
    elif x >= 40 and x <= 49:
        print("C")
    elif x >= 50 and x <= 59:
        print("D")
    else:
        print("failed")

else:
    print("Our program only accepts interger values")

print("I will execute either way")