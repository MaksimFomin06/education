count = int(input())
str = input()

dct = {}
for let in str:
    dct[let] = dct.get(let, 0) + 1

left_part = ""
middle = ""
for key in sorted(dct.keys()):
    count = dct[key]
    left_part += key * (count // 2)
    
    if count % 2 != 0 and middle == "":
        middle = key

ans = left_part + middle + left_part[::-1]

print("".join(ans))