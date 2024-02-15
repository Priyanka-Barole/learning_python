# Que- write a python program enter user choise .
# solution-
choise=True
while choise==True:
	var1=int(input("enter value:"))
	fact=1
	for j in range(1,var1+1):
		fact=fact*j
	print(fact)
	user_choise=(input("enter Y for yes and y no:"))
	if user_choise=="Y":
	choise==True
	else:
		user_choise=="y"
		choise==False

