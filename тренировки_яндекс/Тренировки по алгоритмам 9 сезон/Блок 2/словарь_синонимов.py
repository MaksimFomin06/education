n = int(input())
dct = {}

for i in range(n):
    w1, w2 = input().split()
    if not dct.get(w1):
        dct[w1] = w2
        dct[w2] = w1

word = input()

print(dct[word])