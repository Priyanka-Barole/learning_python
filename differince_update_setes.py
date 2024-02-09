# Que. Write python program update the first set with items thst don't exist in the second set.
'''set1 = {10, 20, 30}
set2 = {20, 40, 50}
set1.difference_update(set2)
print(set1)
'''

# Que. Write python program Return a set of elements present in set A or B, but not both.
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.symmetric_difference(set2)
print(set1)
