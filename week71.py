def fib(last):
    a, b = 0, 1
    while b <= last:
        print(b, end=' ')
        a, b = b, a+b
    print()

if __name__ == "__main__":
    fib(20)