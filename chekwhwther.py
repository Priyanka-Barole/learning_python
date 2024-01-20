# Que-write a python program creat last digit is number divisible by 3 or not.
num=int(input("enter the number:"))
result=num%10

if result%3==0:
	print("last digit is number divisible by 3")
else:
	print("last digit is not divisible number by 3")
