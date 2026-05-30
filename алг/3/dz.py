miniproverka
1) 10
2) первый элемент с конца
3) первое - это проходка по элементам списка, а второе по индексам (хотя точнее сказать что выполнится количество итераций равное длине списка)
4) потому что будет выход за пределы списка
5) добавляет в конец списка
дз
1)
n = int(input()) #можно было и без этого
lst = list(map(int, input().split()))
print(sum(lst))
2)
n = int(input())
lst = list(map(int, input().split()))
ans = len(list(filter(lambda elem: elem % 2 == 0, lst)))
print(ans)
3)
n = int(input())
lst = list(map(int, input().split()))
lst.sort()
print(lst[-1])
4)
n = int(input())
lst = list(map(int, input().split()))
prev = lst[0]
count = 0
for ind in range(1, len(lst)):
    now = lst[ind]
    if now > prev:
        count += 1
    prev = now
print(count)
5)
n = int(input())
lst = list(map(int, input().split()))
new_lst = list(filter(lambda elem: elem > 0, lst))
print(*new_lst)