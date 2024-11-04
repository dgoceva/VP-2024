def NFact(N:int=5)->float:
    """
    Compute the factorial of a given number N using iteration.
    """
    if N < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif N == 0:
        return 1
    else:
        result = 1
        for i in range(1, N+1):
            result *= i
        return result