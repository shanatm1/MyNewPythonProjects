
#with open('test.txt') as file:
   # print(file.read())

#print(file.closed)   #this will close your file automatically once u read

#bymistake if we would write a wrong extension name we can handle the exception to
#continuous execution of the program
try:
    with open('test.tx') as file:
        print(file.read())
except FileNotFoundError:
    print("please write  the correction extension of a file!")

