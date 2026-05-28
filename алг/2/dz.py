
минипроверка:
1) 0
1
2
3
2) (1, н) - это не включительно н, а (1, н + 1) - это включительно н
3) чтобы задать начальное значение, если обьъявлять ее в цикле, то значение будет каджый раз сбрасываться
4) могут быть отрицательные числа, или максимум будет меньше 0
5) условно ломает цикл

дз:
1) 
n = int(input())
summ = 0
for i in range(1, n + 1):
    summ += i
print(summ)
2) 
count = 0
n = int(input())
for i in range(n):
    num = int(input())
    if num > 0:
        count += 1
print(count)

3)
n = int(input())
maxi = int(input())
for i in range(n-1):
    num = int(input())
    if num > maxi:
        maxi = num
print(maxi)

4) 
ans = "NO"
n = int(input())
for i in range(n):
    num = int(input())
    if num == 0:
        ans = "YES"
print(ans)

5) 
count = 0
n = int(input())
for i in range(n):
    num = int(input())
    if num % 3 == 0:
        count += 1
print(count)