cases = int(input())

for i in range(cases):
    n, d = map(int, input().split())
    peopl = []
    for j in range(n):
        t, k = map(int, input().split())
        peopl.append((t, k))

    curr_w = 0
    overf = []
    for j in range(n):
        t, k = peopl[j]
        overf.append(curr_w - t)
        curr_w += k
    suf_max = [0] * (n + 1)
    cur_max = -10**18
    
    for j in range(n - 1, -1, -1):
        if overf[j] > cur_max:
            cur_max = overf[j]
        suf_max[j] = cur_max
        
    suf_max[n] = -10**18

    luchs_pos = n
    
    for pos in range(n + 1):
        if suf_max[pos] + d <= 0:
            luchs_pos = pos
            break
            
    print(luchs_pos + 1)