# Que- Wriite a python program Ask the user for a string and print string is a palindrome or not. 
# solution-

_str=input("enter string:")
_str2=""
for i in reversed (_str):
	_str2=_str2+i
if _str==_str2:

		print("it is palindrome")
else:
		print("it is not palindrome")	