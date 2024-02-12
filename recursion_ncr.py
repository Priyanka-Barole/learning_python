# Que-write a python program create ncr in use to recursion.
# solution-
def factorial(x):
	if x==0:
		return 1
	else:
		return x * factorial(x-1) 	
	
def combination(n,r):
	ans=factorial(n)/(factorial(n-r) * factorial(r))
	return ans	

n=int(input("enter n:"))
r=int(input("enter r:"))
result=combination(n,r)
print(result)	

if int (result)==result:
	print(int(result))
else:
	print(result)




