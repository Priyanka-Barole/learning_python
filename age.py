# write a program to chek whether a person is eligible for voting or not(accept age for age).

age=int(input("enter the age:"))
if age>=18:
	print("eligible for voting")
else:
	print("not eligible for voting")


age_1=int(input("enter the age 1:"))
age_2=int(input("enter the age 2:"))
age_3=int(input("enter the age 3:"))
age_4=int(input("enter the age 4:"))
if age_1>age_2 and age_1>age_3 and age_1>age_4:
	print(" age of old pepole is",age_1 )
elif age_2>age_1 and age_2>age_3 and age_2>age_4:
	print(" age of old pepole is ",age_2)
elif age_3>age_1 and age_3>age_2 and age_3>age_4:		
	print("age of old pepole is ",age_3)
elif age_4>age_1 and age_4>age_2 and age_4>age_3:
	print("age of old pepole is ",age_4)
