n, m  = map(int, input().split())

n_lst = []
m_lst = []

for i in range(n):
    l_i, r_i, x_i = map(int, input().split())
    n_lst.append([l_i, r_i, x_i])

for i in range(m):
    q_i = int(input())

    m_lst.append(q_i)

for i in m_lst:
    ans = 0

    for l_i, r_i, x_i in n_lst:
        if l_i <= i <= r_i:
            if (i - l_i) % 2 == 0:
                ans += x_i
            else:
                ans -= x_i

    print(ans)