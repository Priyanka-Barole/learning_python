# que-write a python program aceept 10 number from the user if the number is odd and than add taht number is list.
lst=[]
for i in range(10):
	num=int(input("enter number:"))
	if num%2!=0:
		lst.append(num)
print(lst)