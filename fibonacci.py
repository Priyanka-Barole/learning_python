# Que- write a python program create fibonacci siris.
# recursion-

def fibonaci(n):
	if n==1:
		return 0
	elif n==2:
		return 1
	else:
		return(fibonaci(n-1)+fibonaci(n-2))
n=int(input("enter n:"))
for i in range(1,n+1):
	print(fibonaci(i))		
