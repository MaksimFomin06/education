n, m, k = map(int, input().split())
windows = [[] for _ in range(n)]
curr_win = 0
clipboard = []

for _ in range(m):
    cmd = input()
    
    if cmd == "Next":
        curr_win = (curr_win + 1) % n
        
    elif cmd == "Backspace":
        if windows[curr_win]:
            windows[curr_win].pop()
            
    elif cmd == "Copy":
        clipboard = windows[curr_win][-k:]
        
    elif cmd == "Paste":
        windows[curr_win].extend(clipboard)
        
    else:
        windows[curr_win].append(cmd)

res_list = windows[curr_win][-k:]
result = "".join(res_list)

if result == "":
    print("Empty")
else:
    print(result)
