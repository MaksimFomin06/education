count = int(input())
capitals = list(map(int, input().split()))
if count == 1:
    print(1)
elif capitals[-1] == capitals[0]:
    print(*[0 for i in range(count)], sep='\n')
else:
    last_null = 0
    capital = 0
    for i in range(count - 1):
        capital += capitals[i]
        if capital > capitals[i+1]:
            pass
        else:
            last_null = i
    print(*[0 for i in range(last_null+1)], sep='\n')
    print(*[1 for i in range(last_null, count-1)], sep='\n')
