def main():
    p, v = map(int, input().split()) 
    q, m = map(int, input().split())
    
    Vl, Vr = p - v, p + v
    Ml, Mr = q - m, q + m
    minL = min(Ml, Vl)
    minR = min(Mr, Vr)
    maxL = max(Vl, Ml)
    maxR = max(Mr, Vr)
    if maxL <= minR:
        answer = maxR - minL + 1
    elif maxL > minR:
        answer = (Vr - Vl + 1) + (Mr - Ml + 1)

    print(answer) 
if __name__ == "__main__":
    main()