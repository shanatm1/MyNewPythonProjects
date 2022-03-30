import os


source = "happy.txt"
destination = "C:\\Users\\shana\\Desktop\\happy.txt"


try:
    if os.path.exists(destination):
        print("the file is already there")
    else:
        os.replace(source,destination)
        print(source +" file is moved")
except FileNotFoundError:
    print("file not found")