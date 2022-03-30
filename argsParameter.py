#args = parameter that will pack all argumentsinto a tuple , its useful so that
# afunction can accept varying amount of arguments

def add(num1, num2):
    sum = num1 + num2
    return sum
print(add(3, 6))  # this is the case when you have 2 numbers to add and u gave 2 arguments and parameters

#below is the case when you have lots f numbers to add

def add1(*args): # we can name anything instead of args
    sum = 0
    for i in args:
        sum += i
    return sum
print(add1(1,2,3,4,5))

