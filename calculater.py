# Que- write a python program create a simple calcuater.
num_1=float(input("enter the number 1:"))
num_2=float(input("enter the number 2:"))
opretor=input("enter the opretor")
if opretor=="+":
	print(num_1+num_2)
elif opretor=="-":
	print(num_1-num_2)
elif opretor=="*":
	print(num_1*num_2)
elif opretor=="%":
	print(num_1%num_2)
elif opretor=="//":
	print(num_1//num_2)
elif opretor=="**":
	print(num_1**num_2)
elif opretor=="/":
	print(num_1/num_2)	
else:
	print("invalid opretor")




