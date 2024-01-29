#Traversing a python Dictionary
A={1:"one",2:"Two",3:"Three"}
for i in A:
	print(i,"->",A[i])

# append value in python Dictionary
A={1:"one",2:"Two",3:"Three",}
A[4]="four"
print(A)

#update method
A={1:"one",2:"Two",3:"Three",}
B={1:"Amit",2:"sunil",5:"Lata",6:"suman",7:"Ravi"}
A.update(B)
print(A)

nam_roll={10:"Amit",20:"sunil",30:"Lata",40:"suman",50:"Ravi"}
for i in nam_roll:
	print(i,"->",nam_roll[i])

#update value in python Dictionary	
nam_roll={10:"Amit",20:"sunil",30:"Lata",40:"suman",50:"Ravi"}
nam_roll[2]='Ram'
print(nam_roll)

