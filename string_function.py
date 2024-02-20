# Que-Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
# solution-
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
 
s = input("enter string:")
 
print("string is : ", end="")
print(s)
 
print("The reversed string is : ", end="")
print(reverse(s))
