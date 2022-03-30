#set isa collection which is unordered and unindexed, no duplicate values

utensils = {"spoon", "fork", "knife", "knife", "knife"}
dishes = {"bowl", "cup", "plate", "knife"}
#dishes.update(utensils)
#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()

#dinner_table =utensils.union(dishes)
#for x in dinner_table:
 #   print(x)

print(dishes.difference(utensils))
print(utensils.intersection(dishes))