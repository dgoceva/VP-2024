import week71
from week71 import fib2
import week6 as wk
# from week6 import *
from datetime import datetime
from week6 import mysum,mysum1
from week2.week77 import week74

def NFact(n:int=5)->float:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0:
        return 1
    else:
        return n * NFact(n-1)
    

if __name__ == "__main__":
    import sys
    print(sys.path)
    week71.fib(100)
    print(fib2())
    print(wk.fib31(15))
    print(type(fib2))
    fibb = wk.fib31
    print(fibb(25))
    print(NFact())
    # print(NFact(-1))
    factoriel = NFact
    print(factoriel(0))
    print(datetime.now())
    print(mysum(1,2,3,4,5))
    print(mysum1([1,2,3,4,5,6,7,8,9]))
    week74.fib(100)