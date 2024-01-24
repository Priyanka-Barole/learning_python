# que-write a python program to accept five number for user the stor in tuple.
T1=()
result=0
while result<5:
	num=int(input("enter number:"))
	T1=T1+(num,)
	result=result+1
print(T1)