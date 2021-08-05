# """declaring variables"""

# u = 1
# y: str = 'hello'

# """control"""

# if(u == 1):
#     print(u)
# else:
#     print('no')

# """functions"""

# def t(input: str):
#     print(input)

# t("hello")

# def number(x: int) -> int:
#     return x

# print(1 + number(9))

# def f(i: int, z) -> int:
#     return i + z(10)

# print(f(1, number))

# """classes"""

# class myClass:
#     def __init__(self):
#         self.i = 0

# z = myClass()

# """loops"""

# fish = ["pike", "tuna", "salmon"]

# for x in fish:
#     print(x)

# for x in range(7):
#     print(x)



# """write fizzbuzz"""

# def fizzbuzz(number: int):
#     s: str = ''
#     if(number % 3 == 0):
#         s += 'fizz'
#     if(number % 5 == 0):
#         s += 'buzz'
#     return s

# for x in range(16):
#     print(x, fizzbuzz(x))


"""Dicts"""

cars = {
    "impala": 400,
    "tesla": 500
}
## accessor has to be this
print (cars.impala)

"""sets"""

vowels = {"a", "e", "i", "o", "u"}

"e" in vowels

"""arrays/lists"""

fruit = ["apples", "peaches", "kiwis"]

fruit.append("oranges") ## adds to end of list

print(fruit.count())

