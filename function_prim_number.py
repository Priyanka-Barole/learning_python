# Que-weite a python script to identify prime number take user input.
# solution-
def primes(i):
	if i==1:
		return False
		
	else:
		for a in range(2,i):
			if i%a==0:
				return False	
				break
		else:
			return True
				
n=int(input("enter n :"))
for j in range(1,(n+1)):
	var_1=primes(j)
	if var_1==True:
		print(j,"it is prime number" )
	else:
		print(j,"it is  non prime number")


