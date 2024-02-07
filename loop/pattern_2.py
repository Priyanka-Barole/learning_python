# Que- write a python program print given pattern
# for n=3  for=4
#     123   1234
#     123   1234
#     123	1234
#           1234
n=int(input("enter the n:"))
for _ in range(n):
	for i in range(1,n+1):
		print(i,end= "")
	print()