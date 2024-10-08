# data1,data2,data3 = map(int,input("Data: ").split(","))
# print(data1,data2,data3)

for i in range(5):
    print(i,end=' ')
print()

data = []
for i in range(5):
    data.append(i)
print(data)

# data = []
# while True:
#     num = int(input("x="))
#     if num==0:
#         break
#     data.insert(0,num)
# print(data)

import random
data = []
for i in range(10):
    data.append(random.randint(-10,10))
print(data)

# conditionals
# X     Y       not X       X or Y      X and Y
# False False   True        False       False
# False True    True        True        False
# True  False   False       True        False
# True  True    False       True        True

result = []
for x in data:
    if x>0 and x%2==0:
        result.append(x)
print(result)

for i in range(len(data)):
    print(i)

for x in data:
    if x%2!=0 and x<0:
        data.remove(x)
print(data)

data = [x for x in range(1,10,2)]
print(data)

data = [int(x) for x in input("data:").split()]
print(data)

print(sum(data))
print(max(data))
print(min(data))

import numpy as np

print(np.prod(data))

data1 = [x for x in np.arange(1,10,0.1)]
print(data1)

data = [x for x in range(0,10,2)]
print(data)

print(data[:])
print(data[2:])
print(data[1:3])
print(data[:2])
print(data[-1])
print(data[-1:-2])
print(data[-2:-1])

data.sort(reverse=True)
print(data)

print(sorted(data))
print(data)

# dd-mm-yyyy
import datetime

datestr = input("Date[dd-mm-yyyy]: ")
bdate = datetime.datetime.strptime(datestr,"%d-%m-%Y")
print(bdate)
delta = datetime.timedelta(days=1000)
print(delta)
print(bdate+delta)
print((bdate+delta).strftime("%d-%m-%Y"))