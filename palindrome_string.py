# Que-write a python program fonction tacke checkes if a given string is a palindrome or not.
def check_palindrome(_str):
	clean_str=(_str.replace("","")).lower()
	reverse_str=clean_str[::-1]
	return clean_str==reverse_str
_str=input("enter a string:")
if check_palindrome(_str):
	print("it is palindrome string")
else:
	print("it is not palindrome")		