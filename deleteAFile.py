import os

source ="C:\\Users\\shana\\Desktop\\happy.txt"
destination = "C:\\Users\\shana\\MyNewPythonProjects\\happy.txt"

try:
    if os.path.exists(destination):
        print("the file is already there")
    else:
        os.replace(source,destination)
        print(source +" file is moved")
except FileNotFoundError:
   print("file not found")
try:    
    os.remove("happy.txt")   #delete a file
    #os.rmdir("path")         #delete an empty directory
    #shutle.rmtree(path)      #delet a directory containing file
except FileNotFoundError:
    print("cant see the file to remove")
