# Que-write a python program given three arrays we have to find common element in three sorted list using sets.
L1=[1,5,5]
L2=[3,4,5,5,10]
L3=[5,5,10,20]

#typecsting in to set

s1=set(L1)
s2=set(L2)
s3=set(L3)

s1s2 =s1.intersection(s2)
new_sets=s2.intersection(s3)
# type casting in to list 
new_list=list(new_sets)
print(new_list)

#accessing for loop
name={"Jhon","mary","Dave"}
for x in name:
	print(x)

#cheak if an item exists in a set
name={"Jhon","mary","Dave"}
if "Ria" in name:
	print("Ria is in the set")

# add elements in set
name={"Jhon","mary","Dave"}
name.add("Ria")
print(name)

# add another sequence in a set
names={"Jhon","mary","Dave"}
name_der=("sia","kia")
names.update(name_der)

# removing element from a set
names.remove("sia")
print(names)

# joining 2 set
s1={'a','b','c'}
s2={'d','e','a'}
print(s1,s2)

s3=s1.union(s2)
print(s3)

s1.update(s2)
print(s1)

# keep only duplicates while joining
s1.intersection_update(s2)
print(s1)

# keep all values exseest duplicates
s1.symmetric_difference_update(s2)
print(s1)
