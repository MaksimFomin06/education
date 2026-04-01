n = int(input())
max_l = None
min_r = None

for i in range(n):
    x_i, d_i = map(int, input().split())
    left = x_i - d_i
    right = x_i + d_i

    if max_l is None:
        max_l = left
        min_r = right
    else:
        max_l = max(max_l, left)
        min_r = min(min_r,right)

if max_l <= min_r:
    print(min_r)
else:
    print(-1)