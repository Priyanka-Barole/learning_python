# Expression

var1=input("enter the Expression:")
var2=[]
temp=""
opretor_list=["+","-","*","%","/"]
for i in var1:
	if i not in opretor_list:
		temp=temp+i
	else:
		var2.append(temp)
		temp=""
		var2.append(i)
else:
	var2.append(temp)

print("input string:",var1)
print("split string:",var2)	

for i in range(len(var2)):
	if var2[i] == "":
		print("invalid Expression")
		break
