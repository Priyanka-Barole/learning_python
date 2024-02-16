# list overleap-
# solution-
def intrsection(lst1,lst2):
    return list(set(lst1) & set(lst2))



lst1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(intrsection(lst1,lst2))