players = {}
l_score = 0
r_score = 0
n = int(input())

for i in range(n):
    name = input()
    players[name] = 0

count = int(input())

for i in range(count):
    score, name = input().split()
    left, right = score.split(":")
    left = int(left)
    right = int(right)

    score = left - l_score + right - r_score
    players[name] += score

    l_score, r_score = left, right

ans = max(players, key=players.get)

print(ans, players[ans])