n = int(input())
lst = list(map(int, input().split()))

prfx = [0 for i in range(n + 1)]
for i in range(1, n + 1):
    prfx[i] = prfx[i - 1] + lst[i - 1]

q = int(input())
x = int(input())

x_lst = [0 for i in range(2 * q)]
x_lst[0] = x
for i in range(1, 2 * q):
    x_lst[i] = (11173 * x_lst[i - 1] + 1) % 1000000007

ans = 0
for i in range(q):
    idx1 = x_lst[2 * i] % n
    idx2 = x_lst[2 * i + 1] % n
    
    l, r = min(idx1, idx2), max(idx1, idx2)
    ans += prfx[r + 1] - prfx[l]

print(ans)
