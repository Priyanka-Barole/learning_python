Que-Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
import random
n = random.randint(1,9)

while True:
	user_input=int(input("enter user guess 1 to 9 :"))
	if user_input < n:
		print ("guess is low")
	elif user_input > n:
		print ("guess is high")
	else:
		print("you guess is right")
		break

			    