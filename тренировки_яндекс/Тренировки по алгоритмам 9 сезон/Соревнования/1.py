from collections import Counter

n = int(input())
all_str = []

for i in range(n):
    str = input()
    all_str.append(str)

count = 0

for k in range(len(all_str[0]) + 1):
    prefixes = []
    for str in all_str:
        prefixes.append(str[:k])
    
    dct = dict(Counter(prefixes))
    
    pairs = 0
    for value in dct.values():
        pairs += value // 2
    
    if pairs >= n // 2:
        count = k

print(count)