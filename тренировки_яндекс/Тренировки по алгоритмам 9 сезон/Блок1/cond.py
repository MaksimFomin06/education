t_r, t_c = map(int, input().split())
mode = input()

if t_c == t_r:
    ans = t_r
elif mode == "freeze":
    if t_r <= t_c:
        ans = t_r
    else:
        ans = t_c
elif mode == "heat":
    if t_r >= t_c:
        ans = t_r
    else:
        ans = t_c
elif mode == "auto":
    ans = t_c
elif mode == "fan":
    ans = t_r

print(ans)