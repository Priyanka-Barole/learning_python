# pass By value
def addone(x):
	x=x+1
	print("inside function",x)

x=5
addone(x)
print("outside function ",x)

#  pass By refrence
def modifiiylist(lst):
	lst.append(4)
	print("inside function",lst)

lst=[1,2,3]
modifiiylist(lst)
print("outside function",lst)		

#  pass By refrence
def modifiiylist(lst):
 	lst=[5,6,7]
 	print("inside function",lst)
lst=[1,2,3]
modifiiylist(lst)
print("outside function",lst)	

def addone(x):
	x=x+1
	return


x=5
addone(x)
print(x)


def addlist(list):
	list.append(8)
	return


list = []
addlist(list)
print(list)
