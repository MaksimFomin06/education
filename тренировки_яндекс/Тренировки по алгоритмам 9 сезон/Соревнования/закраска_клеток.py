moves = input()
x, y = 0, 0
dct = {}
dct[(x, y)] = 1
for move in moves:
    if move == "U":
        y += 1
    if move == "R":
        x += 1
    if move == "D":
        y -= 1
    if move == "L":
        x -= 1

    if (x, y) in dct:
        dct[(x, y)] += 1
    else:
        dct[(x, y)] = 1

ans = 0
for key in dct:
    if dct[key] > 1:
        ans += 1

print(ans)