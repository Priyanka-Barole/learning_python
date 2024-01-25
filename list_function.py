#Adding element to a list 
lst=[10,20,30,40,50]
lst.append(60)
print(lst)

lst=[1,"one",2,"Two",3,"Three"]
lst.append(4)
print(lst)

#list insert
lst=[10,20,30,40,50]
lst.insert(2,60)
print(lst)

lst=["apple","banana","cherry","kiwi"]
lst.insert(3,"mengo")
print(lst)

#list extend
lst=[10,20,30,40,50]
lst2=[100,200]
lst.extend(lst2)
print(lst)

#list extend
lst=["apple","banana","cherry"]
lst2=["kiwi","mengo"]
lst.extend(lst2)
print(lst)
