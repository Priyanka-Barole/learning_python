# Que- write a python program to enter roll number and name of five students and stor dictinoray.
d={}
for i in range(5):
	roll=int(input("enter roll number:"))
	name=input("enter student name:")
	d[roll]=name
print(d)	