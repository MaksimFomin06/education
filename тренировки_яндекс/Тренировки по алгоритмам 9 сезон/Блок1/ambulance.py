from math import ceil


k1, m, k2, p2, n2 = map(int, input().split())

x = ceil(k2 / n2)
y = x * m

alg_pod = k2 // y + 1

if alg_pod != p2:
    print("Невозможно определить подъезд")
if alg_pod == 1:
    alg_et = ceil(k2 / x)
    print(alg_et)
else:
    alg_et = ceil((k2 - y) / x)

if alg_et != n2:
    print("Невозможно опеределить квартиру")

