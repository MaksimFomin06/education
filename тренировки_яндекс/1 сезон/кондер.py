troom, tcond = map(int, input().split())
rezim = input()
ans = troom

if rezim == "freeze":
    if troom > tcond:
        ans = tcond
elif rezim == "heat":
    if troom < tcond:
        ans = tcond
elif rezim == "auto":
    ans = tcond

print(ans)    