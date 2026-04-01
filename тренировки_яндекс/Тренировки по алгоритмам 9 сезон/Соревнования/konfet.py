n = int(input())
p = list(map(int, input().split()))

left = 0
counts = {}
ans = 0

for right in range(n):
    candy = p[right]
    
    if candy in counts:
        counts[candy] += 1
    else:
        counts[candy] = 1
    
    while len(counts) > 2:
        left_candy = p[left]
        counts[left_candy] -= 1
        if counts[left_candy] == 0:
            del counts[left_candy]
        left += 1
    
    if len(counts) == 2:
        current_len = right - left + 1
        if current_len > ans:
            ans = current_len

print(ans)