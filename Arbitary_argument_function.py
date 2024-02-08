#Arbitary argument
def printallnumber(*args):
	_sum=0
	for i in args:
		_sum+=i
	return _sum
output=printallnumber(1,2,3,4,5,6)
print("sum of the number",output)		
