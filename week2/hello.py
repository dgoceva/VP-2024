# print('Hello World!')
# age = int(input())
# print('Age: %d' % age)
# print(f'Age: {age}')
# print("Age: "+str(age))
# print("Age: ", age, " years")

# # read three ints
# num1 = int(input("num1 = "))
# num2 = int(input("num2 = "))
# num3 = int(input("num3 = "))
# print(f"num1 = {num1}, num2 = {num2}, num3 = {num3}")
# print("num1 = {0}, num2 = {1}, num3 = {2}".format(num1, num2, num3))
# num1, num2, num3 = map(int, input("Enter data: ").split())
# print("num1={},num2={},num3={}".format(num1, num2, num3))

# name = input("Name: ")
# print(name.upper(), name.lower(), name.title())

# list
data = [1, 22, 3, -4, 5]
print(data)

data = range(10)
print(data)
data = []
for i in range(0, 10, 2):
    data.append(i)
print(data)

for i in data:
    print(i, end=" ")
print()

for i in range(10, 0, -1):
    data.insert(0, i)

print(data)

del data[0]
print(data)
del data[-1]
print(data)
# del data
# print(data)

data.remove(4)
print(data)
if -1 in data:
    data.remove(-1)
print(data)
print(data.pop())
print(data)
# print(data.pop(12))
print(data.pop(2))
print(data)
print(len(data))
print(len("Ivan"))
# data.peek(12)

info = "Hello"+" World!"
print(info)
print(3*info)

print(3+2, 3-2, 3*2, 3/2, 3//2, 3 % 2, 3**2)
print(3 < 2, 3 <= 2, 3 > 2, 3 >= 2, 3 == 2, 3 != 2)
