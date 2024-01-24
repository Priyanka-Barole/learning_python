# que-write a python program enter user difiend number and divisible by 10.
# solution-

num=int(input("enter the number:"))
result=num%10
print(result)



# que-write a program displye all the number wiche are displye by 11 but not by 2 between 100 and 500.
# soltion-
for i in range(100,500):
	if i%11==0 and i%2==0:
		print(i)
