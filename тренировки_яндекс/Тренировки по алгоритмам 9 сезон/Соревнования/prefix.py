n = int(input())
s = input()

prefix_sum = 0
count = {0: 1}

for char in s:
    if char == 'a':
        prefix_sum += 1
    else:
        prefix_sum -= 1
    
    if prefix_sum in count:
        count[prefix_sum] += 1
    else:
        count[prefix_sum] = 1

ans = 0
for c in count.values():
    ans += c * (c - 1) // 2

print(ans)