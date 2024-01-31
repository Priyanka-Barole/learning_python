# Que-write a python program user defind function "tuplesum" which takes a tuple containg five number as an argument and display the sum of all the number.
def tuplesum(T1):
	result=0
	for i in T1:
		result=i+result
	print("sum of all the number",result)
t1=(3,4,5,6,2)
tuplesum(t1)		