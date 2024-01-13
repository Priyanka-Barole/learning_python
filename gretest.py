#write a python  program script to chek gretest number.
#input:enter a frist number and secend number and thard number.
#proces:take a value user difined value.
#1.if n1greter then n2 and n1greter then n3:
#print"n1,is the gretest number"
#2.else n2 greter then n1 and n2 greter then n3:
#print"n2,is the gretest number"
#3.else:print"n3,is the gretest number"

n1=int(input("enter number1:"))
n2=int(input("enter number2:"))
n3=int(input("enter number3:"))
if n1>=n2 and n1>=n3:
	print(n1,"is the gretest number")
elif n2>=n1 and n2>=n3:
	print(n2,"is the gretest number")
else:
	print(n3,"is the gretest number")
