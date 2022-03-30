
name = "shahana"   #global scope(avaible inside and outside function)

def display_name():
    name = "shahana"     #local scope(avaible only inside the function
    print(name)
display_name()


print(name) 