# Que-write a python program create list.
# solution-
lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for x in lst:
    if x< 5: print(x)
print( [ x for x in lst if x<5 ] )