
from collections import deque
import random

# stack
# LIFO = Last In, First Out

stack = []
stack.append(1)
stack.append(2)
stack.append(3)

print(stack)
print(stack.pop())
print(stack)

# queue
# FIFO = First IN, First Out
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
# queue.appendleft(2)
print(queue)

print(queue.popleft())
# print(queue.pop())
print(queue)
# print(queue.peek())

data = [random.randint(-10,10) for i in range(20)]
print(data)

data = []
for i in range(20):
    data.append(random.randint(-10,10))
print(data)

data.reverse()
print(data)
data.sort()
print(data)
data.sort(reverse=True)

negdata = [x for x in data if x < 0]
print(negdata)
print(sum(negdata))
print(sum([x for x in data if x < 0]))
print(sorted(negdata))
print(sorted(negdata, reverse=True))
print(negdata)

print([x for x in data if x>0 and x%2==0])
print(min([x for x in data if x>0 and x%2==0]))

posdata = [x for x in data if x%2!=0]
print(posdata)
maxodd = max(posdata)
print(maxodd)
print(posdata.count(maxodd))
print(posdata.index(maxodd))
print(data)
print(data.index(maxodd))

# print(-3%2) # =1
for i in range(len(data)-1,-1,-1):
    if data[i] < 0 and data[i]%2 != 0:
        data.insert(i+1,data[i]+1)
print(data)

matrix = [[1,2,3],[4,5,6]]
print(matrix)
print(list(zip(*matrix)))

matrix = [[random.randint(1,10) for j in range(3)] for i in range(2)]
print(matrix)
print([[row[i] for row in matrix] for i in range(3)])

# year = int(input("Year: "))
year = 2024
print(year)
while True:
     if len(list(str(year)))==len(set(str(year))):
         break
     year += 1
print(year)
print(set(str(year)))

data = {x for x in "12345678" if int(x) > 3}
print(data)
data = set()
print(type(data))

d = {}
print(type(d))

d = {"name":"John", "age":30, "city":"New York"}
if "age1" in d:
    print(d["age1"])
print(d["age"])

d["age"] = 31
print(d)
d["country"]="USA"
print(d)

for k,v in d.items():
    print(k,v)

for i,v in enumerate(["Zero","One","Two","three"]):
    print(i,v)

print(list(d.keys()))
print(list(d.values()))
print(sorted(list(d.keys())))

data = {x:x**2 for x in range(10)}
print(data)

for i in reversed(range(10)):
    print(i,data[i])

keys = [1,2,3,4,5,6]
values = [1, 8, 27, 64, 125]

d = dict(zip(keys, values))
print(d)

for k,v in sorted(d.items(), reverse=True):
    print(k,v)

d = {12:10,1:"One","Zero":0,"Two":"2"}
print(d)