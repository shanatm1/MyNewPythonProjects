import time

""""
names = ['nithi', 'nannu', 'sha']
for name in names:
    count = 0
    while count < 5:
        print(name, end=' ')
        count = count + 1
    print()
"""

#print a rectangle pattern with 5 rows and 3 column
""""
rectangle = ['*', '*','*', '*', '*']
for pattern in rectangle:
    count = 0
    while count < 3:
        print(pattern, end = ' ')
        count = count + 1
    print()
"""

# another form

#for name in range(5):
 #   for j in range(3):
  #      print('*', end= ' ')
   # print()

#for i in range(10):
 #   print(i+1)

#for i in range(50, 100+1, 2):
 #   print(i)

#for i in "shana shahana":
 #   print(i)

for seconds in range (10, 0, -1):
    print(seconds)
    time.sleep(1)
print("happy new year")