# Que -Let’s say I give you a list saved in a variable: numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
# solution -

numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(" given list:",numbers)
evens = [num for num in numbers if num % 2 == 0]
print(" even number:",evens)


