lst = list(map(int, input().split()))

prev_elem = lst[0]
ans = "YES"
for elem in range(1, len(lst)):
    if lst[elem] <= prev_elem:
        ans = "NO"
        break
    prev_elem = lst[elem]

print(ans)