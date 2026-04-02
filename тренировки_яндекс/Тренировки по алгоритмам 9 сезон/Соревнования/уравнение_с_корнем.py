a = int(input())
b = int(input())
c = int(input())

if c < 0:
    print("NO SOLUTION")
elif a == 0:
    if b == c ** 2:
        print("MANY SOLUTIONS")
    else:
        print("NO SOLUTION")
else:
    num = c ** 2 - b
    if num % a == 0:
        x = num // a
        if a * x + b >= 0:
            print(x)
        else:
            print("NO SOLUTION")
    else:
        print("NO SOLUTION")