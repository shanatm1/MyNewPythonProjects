
text1 = "The text has been overwrittened"

#we can also append a file with existed  file by writing 'a' instead of'w' below
with open('text1.txt','w') as file:
    file.write(text1)