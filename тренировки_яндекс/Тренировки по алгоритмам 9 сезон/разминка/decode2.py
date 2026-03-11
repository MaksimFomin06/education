str = input()
length = len(str)
now_let = 0
str += "**"
output = ""

while now_let < length:
    if str[now_let + 2] == "#":
        let = str[now_let:now_let+2]
        now_let += 3
    else:
        let = str[now_let]
        now_let += 1

    output += chr(ord("a") + int(let) - 1)
    
print(output)