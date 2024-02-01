import Arithmetic as Am

print("welcome to priyanka calculater")
print("calculater(+,-,*,/,%,**,//)")

choise=int(input("enter for- \n 1 addition\n 2 subtraction\n 3 multiplication\n 4 divison\n 5 modul\n 6 expontiation\n 7 Floordivison\n:"))

if choise==1:

	var_1=int(input("enter value:"))
	var_2=int(input("enter value:"))
	result=Am.addition(var_1,var_2)
	print("{} + {} = {}".format(var_1,var_2,result))

elif choise==2:

	var_1=int(input("enter value:"))
	var_2=int(input("enter value:"))
	result=Am.subtraction(var_1,var_2)
	print("{} - {} = {}".format(var_1,var_2,result))

elif choise==3:
	var_1=int(input("enter value:"))
	var_2=int(input("enter value:"))
	result=Am.multiplication(var_1,var_2)
	print("{} * {} = {}".format(var_1,var_2,result))

elif choise==4:
	var_1=int(input("enter value:"))
	var_2=int(input("enter value:"))
	result=Am.Divison(var_1,var_2)
	print("{} / {} = {}".format(var_1,var_2,result))

elif choise==5:
	var_1=int(input("enter value:"))
	var_2=int(input("enter value:"))
	result=Am.modul(var_1,var_2)
	print("{} % {} = {}".format(var_1,var_2,result))

elif choise==6:
	var_1=int(input("enter value:"))
	var_2=int(input("enter value:"))
	result=Am.expontiation(var_1,var_2)
	print("{} ** {} = {}".format(var_1,var_2,result))

elif choise==7:
	var_1=int(input("enter value:"))
	var_2=int(input("enter value:"))
	result=Am.Floordivison(var_1,var_2)
	print("{} // {} = {}".format(var_1,var_2,result))



else:
	print("invalid value")
