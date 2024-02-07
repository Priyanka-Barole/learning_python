# Que- write a python program print given pattern.
# for n=3  for n=4
#  *        *  
#  **       **
#  ***      ***
#           ****
n=int(input("enter n:"))
for i in range(1,n+1):
	for j in range(1,i+1):
		print("*",end="")
	print()	