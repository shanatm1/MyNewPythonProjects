# TUPLES IS collections which is ordered and unchangeble used to group together related data

student = ("shana", 34, "female")
print(student.count("shana"))
print(student.index("female"))

for x in student:
    print(x)
if "shana" in student:
    print("shana is here")