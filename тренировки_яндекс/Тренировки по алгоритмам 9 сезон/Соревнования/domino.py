n, m = map(int, input().split())
field = []
for i in range(n):
    str = input()
    field.append(str)

count = 0

for y in range(n):
    for x in range(m):
        if x < m-1 and (field[y][x] != "#" and field[y][x + 1] != "#"):
            count += 1
        if y < n-1 and (field[y][x] != "#" and field[y+1][x] != "#"):
            count += 1

print(count)