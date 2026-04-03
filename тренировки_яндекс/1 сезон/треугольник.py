a = int(input())
b = int(input())
c = int(input())
ans = "NO"
if (a + b) > c:
    if (a + c) > b:
        if (b + c) > a:
            ans = "YES"

print(ans)