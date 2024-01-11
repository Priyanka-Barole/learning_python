#write a python script calculet number aver a user difinend two values
#input:enter intiger frist number and secend number and enter opretor"output"(+,-,*,/,%)
#prosess:take a value user difined value.
# 1.if opretor("Addition")
# 2.elif opretor("subtraction")elif("multiplication")elif("Divison")elif("modulus").
# 3.else then we will find inviled opretion.


frist = int(input ("Enter  frist number:"))
opretor = input("Enter opretor (+,-,*,/,%):")
secend = int(input("Enter secend number:"))

if opretor == "+":
	print(frist+secend)
elif opretor == "-":
	print(frist-secend)
elif opretor == "*":
	print(frist*secend)
elif opretor == "/":
	print(frist/secend)
elif opretor == "%":
	print(frist%secend)
else:
	print("invalid opretor")






