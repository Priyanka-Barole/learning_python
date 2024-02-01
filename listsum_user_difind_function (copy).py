# Que- write a python program which takes a list as an argument and display sum od all the number.
def listsumallnumber(Lst):
	result=0
	for i in Lst:
		result=i+result
	print("sum of all the number",result)
L=input("enter any number:")
listsumallnumber(L)
		
# Que write a python program which takes a number as  an argument and display it's factorial.
def fac(num1):
	if num1==1:
		print("factorial num1")
	else:
		result=1
		for i in range(1,num1+1):
			result=result*i
		print("factorial number",result)
n=int(input("enter any number:"))
fac(n)			
