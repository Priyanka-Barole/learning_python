# Que- write a program to accept a number from 1 to 7 and display the name of the day like 1, for sunday 2,for monday and so on.
num=int(input("enter the number 1 to 7:"))
if num==1:
	print("sunday")
elif num==2:
	print("monday")
elif num==3:
	print("tuesday")
elif num==4:
	print("wednesday")
elif num==5:
	print("friday")
elif num==6:
	print("saturday")
else:
	print("please enter the number 1 to 7")