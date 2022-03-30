#this is a parameter that will pack all arguments in a dictionaries

#def hello(first,middle):
   # print("hello"+" "+first+" "+middle)
#hello("shana","shahana")

#if we want to receive varying parameter

def hello1(**kwargs):
    print("hello"+" "+kwargs['first']+" "+kwargs['last'])   #one way to show names
hello1(first="shana", middle="shahana", last= "tm")

#below is the way we can show many names (let say we need to display the full name of person based on the arguments)
#passing to the function

def hello1(**kwargs):
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")
hello1(title= "ms", first1="shana", middle1="shahana", last1= "tm")

#u can use any name instead od kwargs but the common naming convention is kwargs
def hello1(**names):
    print("Hello",end=" ")
    for key,value in names.items():
        print(value,end=" ")
hello1(title= "ms", first1="shana", middle1="shahana", last1= "tm")