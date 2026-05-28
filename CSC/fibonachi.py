def fibonachi(num):
    fib = [0, 1]
    for i in range(2, num+1):
        fib.append(fib[i-1]+fib[i-2])

    return fib[num]


def main():
    num = int(input())

    print(fibonachi(num))

if __name__ == "__main__":
    main()