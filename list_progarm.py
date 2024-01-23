#question1. write a program to create simple list.
#solution-

list=['a','b','c','d']
for i in list:
	print(i)
	


	
#question2. write a program to create list of the following(take input from user) 
#solution-

list=[]
for i in range(5):
	n1=(input("enter student name:"))
	list.append(n1)
	print(list)	
	
	
	
	
#question3. write a program to create list of the following(take input from user)
#solution-

list=[]
for i in range(5):
	n2=(input("enter any nuber:"))
	list.append(n2)
	print(list)	
	
	



#question4. write a program to accept 10 numbers from the user if the number odd the add thst number to the list .
#solution-

a=[]
for i in range(10):
	num=int(input("enter any number:"))
	if num%2 == 0:
		a.append(num)
		print(a)

		
		
