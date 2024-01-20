# Que- write a python program cheak wheter perfect number wheter not perfect number.
# solution-
num=int(input("enter number:"))
result=0
for i in range(1,num):
	if num%i==0:
		result=result+i
if num==result:
	print("it is a perfect number")
else:
	print("it is a not perfect number")		
