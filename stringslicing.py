#create substring by extracting elements from another string
#index based
name = "Shana Shahana"

first_name = name[0:5]
ex_name = name[:3]
last_name = name[6:13]
funky_name = name[0:13:2]
reversed_name = name[::-1]
reversed_lastname = name[-8:-13]
print(first_name)
print(ex_name)
print(last_name)
print(funky_name)
#SaaSaaa
print(reversed_name)
print(reversed_lastname)

#slice based
website1 = "http://google.com"
website2 = "http://yahoo.com"
slice = slice(7, -4)
print(website1[slice])
print(website2[slice])