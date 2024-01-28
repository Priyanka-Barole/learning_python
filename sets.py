names={"sia","mia","jia"}
print(names)
#lenth in sets
print(len(names))
#cheak data type
print(type(names))
#accessing items of set
for x in names:
	print(x)
#cheak if an item exists i a set
if "sia" in names:
	print("sia is in the set")
#add element set
names.add("Ria")
print(names)
#removing element frome set
names.remove("jia")
print(names)
#add other sequence in a set
names_list=("Ria","Kia")
names.update(names_list)
print(names)
#joine 2 set
s1={'a','b','c'}
s2={'d','e','a'}
print(s1,s2)
#joine 2 set
s3=s1.union(s2)
print(s3)
s1.update(s2)
print(s1)
#keep only duplicate while joinig
s1.intersection_update(s2)
print(s1)
#keep all value except duplicate
s1.symmetric_difference_update(s2)
print(s1)		