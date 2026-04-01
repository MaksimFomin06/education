s = input()
n = len(s)

max_lenght = 1
max_count = 0

for i in range(1, min(n + 1, 100)):
    d = {}
    for j in range(n - i + 1):
        t = s[j:j+i]
        if t not in d:
            d[t] = [-i, 0]
        
        if j > d[t][0]:
            d[t][0] = j + i - 1
            d[t][1] += 1
    
    for t in d:
        count = d[t][1]
        if count > max_count or (count == max_count and i > max_lenght):
            max_count = count
            max_lenght = i

print(max_lenght)