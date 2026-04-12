lst = list(map(int, input().split()))

if len(lst) < 2:
    print(0)
else:
    n = lst[0]
    balls = lst[1:]
    stack = []
    ans = 0
    
    for b in balls:
        if stack and stack[-1][0] == b:
            stack[-1][1] += 1
        else:
            if stack and stack[-1][1] >= 3:
                ans += stack.pop()[1]
                if stack and stack[-1][0] == b:
                    stack[-1][1] += 1
                else:
                    stack.append([b, 1])
            else:
                stack.append([b, 1])
    
    if stack and stack[-1][1] >= 3:
        ans += stack.pop()[1]
        
    print(ans) 