# Que-write a python program to accept percentage form the user and display the grade according to the follwing criteria
math_marks=int(input("enter the math marks:"))
if math_marks>90:
	print("gread,A")
elif math_marks>80 and math_marks<=90:
	print("gread,B")
elif math_marks>70 and math_marks<=60:
	print("gread,c")
elif math_marks>60 and math_marks<=50:
	print("gread,D")
else :
	print("Fail")			
