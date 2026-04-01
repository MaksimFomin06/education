words = input().split()
out = []

for word in words:
    i = len(word) - len(word.lstrip("'"))
    j = len(word) - len(word.rstrip("'"))

    word = word.replace("'", '')

    part1 = word[i:]
    part = part1[:len(part1) - j]
    out.append(part)

print("".join(out))