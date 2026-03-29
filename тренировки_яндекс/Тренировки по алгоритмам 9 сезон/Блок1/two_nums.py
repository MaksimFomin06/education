
data = list(map(int, input().split()))

max1 = -float('inf')
max2 = -float('inf')
min1 = float('inf')
min2 = float('inf')
for x in data:
    if x > max1:
        max2 = max1
        max1 = x
    elif x > max2:
        max2 = x
    if x < min1:
        min2 = min1
        min1 = x
    elif x < min2:
        min2 = x
prod_pos = max1 * max2
prod_neg = min1 * min2
if prod_pos >= prod_neg:
    res = [max1, max2]
else:
    res = [min1, min2]
res.sort()
print(res[0], res[1])