import string


def main():
    s = input()
    letters = list(string.ascii_lowercase)
    dct = dict()
    output = ""
    for i in range(1, 27):
        dct[str(i)] = letters[i-1]

    for i in range(len(s)):
        if i == len(s) - 1:
            if s[i] == "#":
                break
            else:
                output += dct[s[i]]
        elif i == len(s) - 2:
            if (s[i] == "#" or s[i+1] == "#"):
                continue
            else:
                output += dct[s[i]]
        elif s[i] == "#" or s[i+1] == "#":
            continue
        elif s[i + 2] != "#":
            output += dct[s[i]]
        else:
            two = s[i] + s[i + 1]
            output += dct[two]

    print(output)
    

if __name__ == "__main__":
    main()