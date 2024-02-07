# Que- write a python program print given pattern.
# for n=3  for=4
# 1        1
# 12       12
# 123      123
#	       1234

n=int(input("enter the n:"))
for i in range(1,n+1):
	for j in range(1,i+1):
		print(j,end="")
	print()