# 8.que-write a python program find the sum of the digite of the number.
'''num=int(input("enter number:"))
result=0
while(num):
	n=num%10
	result=result+n
	num=num//10
	print("sum of the digite number" ,result)

# 10.que-write a python program find sum of the first digite number.
num=input("enter number:")
result=0
for i in range (len(num)):
	first_digit=int(num[i])
	result=result+frist_digit
print(result)

#11.que-write a python program find multipliation of first digite number.
num=input("enter number:")
result=1
for i in range (len(num)):
	frist_digit=int(num[i])
	result=result*frist_digit
print(result)		