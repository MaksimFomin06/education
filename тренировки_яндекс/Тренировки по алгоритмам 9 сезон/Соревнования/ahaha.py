n = int(input())
str = input()
lengths = 0
prev_symbol = None
count = 0

for elem in str:
    if elem in ["h", "a"]:
        if prev_symbol is None or prev_symbol != elem:
            count += 1
        else:
            count = 1
        lengths = max(lengths, count)
        prev_symbol = elem
    else:
        count = 0
        prev_symbol = None

print(lengths)