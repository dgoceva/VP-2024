import week2.week72


def fib(last:int)->None:
    """ Fibonacci function
    Prints Fibonacci numbers up to the given limit.
    """
    a, b = 0, 1
    while b <= last:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n:int=10)->list:
    """ Fibonacci function
    Returns a list of Fibonacci numbers up to the given limit.
    """
    fib_list = [1, 1]
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list

def increment(start):
    return lambda x: x + start

if __name__ == "__main__":
    import week2
    from week2.week72 import NFact
    from week2 import week72
    # import sys
    # print(sys.version)
    # print(sys.argv)
    # fib(int(sys.argv[1]))
    fib(20)
    print(fib2())
    increment_by_5 = increment(5)
    print(increment_by_5(10))
    data = [(1, "One"), (2, "Two"), (3,"Three"), (4,"Four")]
    data.sort(key=lambda pair: pair[1],reverse=True)
    print(data)
    print(fib.__doc__)
    print(fib.__annotations__)
    print(week2.week72.NFact())
    print(NFact(3))
    print(week72.NFact(4))