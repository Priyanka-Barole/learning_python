# Que-write a python program create prime number use to list.
# solution-
num=int(input("enter number:"))
prime_factors=[]
for i in range(1,num+1):
	if i==1:
		continue
	if num%i==0:
		temp=0
	for j in range(2,i):
		if i%j==0:
			temp=1
		break
	if temp==0:
		prime_factors.append(i)
print(prime_factors)			

