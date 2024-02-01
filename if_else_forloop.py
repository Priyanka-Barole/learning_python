'''var_x=int(input("enter a value:"))
result=1
for i in range(1,var_x+1):
	result=result*i
	print(result)'''


var_1=int(input("enter a value:"))
result=1
if var_1==0 or var_1==1:
	print("factorial of the given is one")
elif var_1 >1:
	for i in range(1,var_1+1):
		result=result*i
	print(result)
elif var_1<0:
	print("invalid number")
