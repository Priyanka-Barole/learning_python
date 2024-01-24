# que-write a program to display all the number which are divisible by 11 but not by 3 between 100 and 500
# solution-

for i in range(100,500):
	if i%11==0 and i%2!=0:
		print(i)
		
		
		

# que-write a program to number from 1 to 20 exept multiple of 2 & 3.
# solution-

for i in range(1,21):
	if i%2!=0 and i%3!=0:
		print(i)	
