def fibonachi(num):
    if num <= 1:
        return num

    a, b = 0, 1
    for _ in range(2, num + 1):
        a, b = b, (a + b) % 10

    return b

def main():
    num = int(input())

    print(fibonachi(num) % 10)
    

if __name__ == "__main__":
    main()