# que-write a python program cheak prime number is prime  or not.
# solution-
num=int(input("enter the number:"))
if num<0:
	print("invelid number")
elif num==1:
	print("1 is not prime number")
elif num==0:	
	print("0 is natural number")	
elif num>1:
	for i in range(2,num):
		if num%i==0:
			print("number is not prime")
			break
	else:
		print("number is prime")			

			
	
	
