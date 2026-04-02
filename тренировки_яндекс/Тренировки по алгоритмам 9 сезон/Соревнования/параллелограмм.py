"""
параллелограммом называется четырехугольник, противоположные стороны которого равны и параллельны.

Программа должна ответить параллелограмм или нет
"""

n = int(input())

for i in range(n):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    first = float(x1 + y1)
    second = float(x2 + y2)
    third = float(x3 + y3)
    thourth = float(x4 + y4)
    if (x1 + x3 == x2 + x4) and (y1 + y3 == y2 + y4):
        print("YES")
    elif (x1 + x2 == x3 + x4) and (y1 + y2 == y3 + y4):
        print("YES")
    elif (x1 + x4 == x2 + x3) and (y1 + y4 == y2 + y3):
        print("YES")
    else:
        print("NO")