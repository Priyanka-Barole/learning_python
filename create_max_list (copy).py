# Que- write a python program given a list print maximum number.
# solution-

lst=[8,6,10,17,89,45]
max_= lst[0]
for i in lst:
	if (i>max_):
		max_= i
print("max value",max_)