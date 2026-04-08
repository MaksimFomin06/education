dct = {}

def deposit(name, sum_val):
    sum_val = int(sum_val)
    dct[name] = dct.get(name, 0) + sum_val

def withdraw(name, sum_val):
    sum_val = int(sum_val)
    dct[name] = dct.get(name, 0) - sum_val

def balance(name):
    if name in dct:
        print(dct[name])
    else:
        print("ERROR")

def transfer(name1, name2, sum_val):
    sum_val = int(sum_val)
    if name1 not in dct:
        dct[name1] = 0
    if name2 not in dct:
        dct[name2] = 0
    
    dct[name1] -= sum_val
    dct[name2] += sum_val    

def income(p):
    p = int(p)
    for client in dct:
        if dct[client] > 0:
            dct[client] += (dct[client] * p) // 100

with open("input.txt", "r", encoding="utf-8") as file:
    for line in file:
        inp = line.split()
        
        cmd = inp[0]
        if cmd == "DEPOSIT":
            deposit(inp[1], inp[2])
        elif cmd == "WITHDRAW":
            withdraw(inp[1], inp[2])
        elif cmd == "BALANCE":
            balance(inp[1])
        elif cmd == "TRANSFER":
            transfer(inp[1], inp[2], inp[3])
        elif cmd == "INCOME":
            income(inp[1])
