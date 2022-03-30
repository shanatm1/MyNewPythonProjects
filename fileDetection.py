import os

path = "C:\\Users\\shana\\Desktop\\folder"

if os.path.exists(path):
    print("this location is exist!")
    if os.path.isfile(path):
        print("this is a file")
    elif os.path.isdir(path):
        print("that is a folder")
else:
    print("that location doesnt exist")