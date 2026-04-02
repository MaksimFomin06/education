field = []
n, m = map(int, input().split())
for i in range(n):
    str = list(map(int, input().split()))
    field.append(str)

end_row, end_str = n, m
now_row, now_str = 0, 0
count = field[0][0]
while now_row != end_row and now_str != end_str:
    left = field[now_row][now_str + 1]
    bottom = field[now_row + 1][now_str]

    if left <= bottom:
        count += left
        now_str += 1
    else:
        count += bottom
        now_row += 1

print(count)