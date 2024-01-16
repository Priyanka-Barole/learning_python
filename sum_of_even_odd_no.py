# 1 Que-write python program to display sum of odd number and even number that fall between 12 and 37(including both number)

result_1=0
result_2=0
for i in range(12,37):
	if i%2==0:
		result_1=result_1+i
	else:
		result_2=result_2+i
		print("sum of odd number",result_1 )
		print("sum of even number",result_2)	