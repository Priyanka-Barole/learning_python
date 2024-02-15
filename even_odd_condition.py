# Que-write a python program print even odd number.
# solution-
num =int(input("Enter a number: "))
num_2 = num % 2
if num_2 > 0:
    print("odd number")
else:
    print("even number")