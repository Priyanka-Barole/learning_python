# que-write a python program to find the average of all  the numbers stored in given list L=[5,10,20,25] without using inbuilt fuction(sum() and len())
lst=[5,10,20,25]
_sum=0
_len=0
for i in lst:
	_sum=_sum+i
	_len=_len+1
print("average of all numbers",_sum/_len)
