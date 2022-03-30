#Its a moethod that gives users more control when displaying output

animal = "cow"
items = "moon"
message1 = "nannu"
message2 = "nithi"

print("The"+" "+animal+" "+"jumped over the"+" "+ items)

#we can show the same message in another way
print("The {} jumped over the {}".format(animal,items))    #this is called format fields,they
#function as a place holder for values or a variable

print("I love {} and {}".format(message1,message2))
print("I love {1} and {0}".format(message1,message2))   #positional arguments
print("I love {name1} and {name2}".format(name1 = "uppa",name2 ="aayina"))   #keyword arguments arguments

#we can write the above in a more simple way
sister1 ="Ithata"
sister2 ="Thanji"
text= "I want to meet {} and {}"
print(text.format(sister1,sister2))

#How can we format a number varibale

number = 3.14159

print("The number pie is {:.2f}".format(number))  #this will display only 2 digits after the decimal


