#11.que-write a python program find multipliation of first digite number.
num=input("enter number:")
result=1
for i in range (len(num)):
	frist_digit=int(num[i])
	result=result*frist_digit
print(result)		