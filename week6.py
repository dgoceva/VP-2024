def fib(last):
    a, b = 0, 1
    while b <= last:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n=5):
    fib_list = [0, 1]
    for i in range(1, n):
        fib_list.append(fib_list[i-1] + fib_list[i])
    return fib_list[1:]

def fib3(n=5,L=[]):
    pass
#     if n <= 0:
#         return L
#     elif n == 1:
#         return L + [1]
#     elif n == 2:
#         return L + [1, 1]
#     else:
#         print(L,n)
#         # return fib3(n-1, L + [L[-1] + L[-2]])

def fib4(n=5,fib_list=[]):
    fib_list = [1, 1]
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list

def createList(n,L=[]):
    L.append(n)
    return L

def createList1(n, L=None):
    if L is None:
        L = []
    L.append(n)
    return L

def func1(*arg1):
    print(arg1)
    return func2(arg1)

def func2(*arg1):
    arg2 = list(arg1)
    arg2= arg2 + list(*arg1)
    arg2.append([-1,-2,-3])
    arg2 += [-1,-2,-3]
    print(arg2)
    return arg2

def passParams(pos_only, /, standard, *, key_word_only):
    print(pos_only, standard, key_word_only)
    return standard + key_word_only

def passParams1(pos1,pos2,pos3,/):
    print(pos1, pos2, pos3)
    return pos1 + pos2 + pos3

def passParams2(*,key1,key2,key3):
    print(key1, key2, key3)
    return key1 + key2 + key3

def mysum(*list):
    return sum(list)

def mysum1(list):
    return sum(list)

def dict(**kwarg):
    print(kwarg)
    return {k:v for k, v in kwarg.items()}

def search(name,dict):
    return name in dict

if __name__ == "__main__":
    print("Hello, World!")
    print(fib(100))
    fib(1000)

print(fib2(10))
print(fib2())
print(fib4())
fib_list = None
fib4(10,fib_list)
print(fib_list)
print(fib4())
print(fib4(3))

print(createList(1))
print(createList(2))
print(createList(22))

print(createList1(1))
print(createList1(2))
print(createList1(22))  
print(fib3())

print(func1(1,2,3,4,5))

print(passParams(1,22,key_word_only=13))
print(passParams(11,standard=33,key_word_only=55))

print(passParams1(1,2,3))
print(passParams1(22,33,44))

print(passParams2(key1=1,key2=2,key3=3))
print(passParams2(key1=11,key2=22,key3=33))

print(mysum(1,2,3,4,5))
print(mysum1([1,2,3,4,5]))

print(dict(**{"one":1,"two":2}))

print(search(name="name",dict={"one":1,"name":"Ivan"}))