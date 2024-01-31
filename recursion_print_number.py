# Que- write a python program to print number from n to 1.

def printnumber(n):
	if n==1:
		return
	print(n)
	printnumber(n-1)
printnumber(100)

# Que- write a python program to print number from 1 to n.
def printnumber(n):
	if n==1:
		return 
	printnumber(n-1)
	print(n)
printnumber(8)	
		

