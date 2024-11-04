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