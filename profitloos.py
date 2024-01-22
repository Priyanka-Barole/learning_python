# Que- write a python program acepte cost prics and enter the seling prics if a seling prics greatest cost prics else seling prics lees then cost prics we have profit amd we have loos.
# solution-
cost_prics=int(input("enter the cost_prics:"))
seling_prics=int(input("enter the seling_prics:"))
if seling_prics>cost_prics:
	profit=seling_prics-cost_prics
	print("we be have profit")
elif seling_prics<cost_prics:	
	loos=cost_prics-seling_prics
	print("we be have loos")
	
