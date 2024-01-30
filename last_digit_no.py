# que- write a python program enter any number last digit number divisible by 10 if last digit divisible by 3 print divisible else not divisible.
num=int(input("enter any number:"))
last_digit=num%10
if last_digit%3==0:
	print("Divisible")
else:
	print("Not divisible")
