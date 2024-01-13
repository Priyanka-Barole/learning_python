#problam stetment:writ the python script to idintify that user given
#input:enter a intiger value output:"even"or "ood"
#process: 1. take a value and assigment a user difined value .
# 2. calculate the reminder of value when divide by 2.
# 3. if a reminder is o then value is even.
# 4. else value is odd.

#reletionship operator: ==,>=,<=,>,<,!=

value  = int(input("enter a value : "))
reminder = value % 2
if reminder == 0:
	print("even")
else:
	print("odd")

#problam satetmet:writ the python script to idintify that user given.
#input:enter the intiger value output:"your to young to marry""and "you are to old to marry"and "we will find parfect match for you" 
#process: 1.take a value and user difined value.
# 2. if a age of age<18: then you are to young to marry.
# 3. elif a age>60: then you are to old marry.
# 4. else then we will find parfect match for you.

#reletionship operatior:

age = int(input("enter your age"))
if age < 18:
 print('you are to young to marry')
elif age > 60:
 print('you are to old to marry')
else:
 print('we will find parfect match for you')	