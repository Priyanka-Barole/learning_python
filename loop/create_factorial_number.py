# que-write a python program factorial givin of number.
# solution-
var_1=int(input("enter the value:"))
result=1
if var_1==0 or var_1==1:
	print("factorial of the given is no.")
elif var_1>1:
	for i in range(1,var_1+1):
		result=result*i
		print(result)
			