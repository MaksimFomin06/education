dct = {}
n = int(input())
for part in range(n):
    m = int(input())
    for i in range(m):
        lang = input()
        if lang in dct.keys():
            dct[lang] += 1
        else:
            dct[lang] = 1

ans1 = [key for key, value in dct.items() if value == n]
print(len(ans1), *ans1, sep='\n')

ans2 = dct.keys()
print(len(ans2), *ans2, sep='\n')