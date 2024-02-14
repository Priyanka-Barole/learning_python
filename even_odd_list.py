# Que- write a python program add even odd number print to list.
# solution-
num=int(input("enter the number:"))
even=[]
odd=[]
for i in range(1,num):
	if i%2==0:
		even.append(i)
	else:
		odd.append(i)
print("even is:",even)
print("odd is :",odd)	