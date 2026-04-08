dct = {}

with open("input.txt", "r", encoding="utf-8") as file:
    for line in file:
        surname, pos, count = line.split()
        count = int(count)

        if surname not in dct:
            dct[surname] = {pos: count}
        elif pos not in dct[surname]:
            dct[surname][pos] = count
        else:
            dct[surname][pos] += count

for key in sorted(dct.keys()):
    print(f"{key}:")
    for elem in sorted(dct[key].keys()):
        print(f"{elem} {dct[key][elem]}")