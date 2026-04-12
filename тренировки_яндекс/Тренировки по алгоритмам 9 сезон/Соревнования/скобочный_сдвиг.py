s = input()
n = len(s)

if n == 0:
    print("YES")
elif n % 2 != 0:
    print("NO")
else:
    ans_s = "NO"
    for i in range(n):
        shifted = s[i:] + s[:i]
        stack = []
        is_ok = True
        
        for char in shifted:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if not stack:
                    is_ok = False
                    break
                last = stack.pop()
                if char == ')' and last != '(':
                    is_ok = False
                    break
                if char == ']' and last != '[':
                    is_ok = False
                    break
                if char == '}' and last != '{':
                    is_ok = False
                    break
        
        if is_ok and len(stack) == 0:
            ans_s = "YES"
            break
            
    print(ans_s)