# que- write a python program tp accept dicimel number and display its binary number.
num=int(input("enter number:"))
lst=[]
while(num):
	n=num%2
	lst.append(n)
	num=num//2
for i in range(len(lst)-1,-1,-1):
	print(lst[i],end="")	