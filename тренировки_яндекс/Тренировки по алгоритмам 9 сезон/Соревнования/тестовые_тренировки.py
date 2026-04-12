n = int(input())
true_ans = input()
m = int(input())
responses = []
for _ in range(m):
    responses.append(input())

res_pairs = []

for i in range(m):
    for j in range(i + 1, m):
        s1 = responses[i]
        s2 = responses[j]        
        c1_total = 0
        c1_match = 0
        w1_total = 0
        w1_match = 0
        c2_total = 0
        c2_match = 0
        w2_total = 0
        w2_match = 0
        
        for k in range(n):
            if s1[k] == true_ans[k]:
                c1_total += 1
                if s1[k] == s2[k]:
                    c1_match += 1
            else:
                w1_total += 1
                if s1[k] == s2[k]:
                    w1_match += 1
                    
            if s2[k] == true_ans[k]:
                c2_total += 1
                if s2[k] == s1[k]:
                    c2_match += 1
            else:
                w2_total += 1
                if s2[k] == s1[k]:
                    w2_match += 1
        
        is_i_ok = (c1_match > c1_total / 2) and (w1_match > w1_total / 2)
        is_j_ok = (c2_match > c2_total / 2) and (w2_match > w2_total / 2)
        
        if is_i_ok and is_j_ok:
            res_pairs.append((i + 1, j + 1))

print(len(res_pairs))
for p in res_pairs:
    print(p[0], p[1])