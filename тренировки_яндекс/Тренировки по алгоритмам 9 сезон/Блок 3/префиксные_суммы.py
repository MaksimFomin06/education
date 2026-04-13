n = int(input())
lst = list(map(int, input().split()))
prfx = [0 for i in range(len(lst) + 1)]
for i in range(1, len(prfx)):
    prfx[i] = prfx[i - 1] + lst[i - 1]

print(*prfx[1:])