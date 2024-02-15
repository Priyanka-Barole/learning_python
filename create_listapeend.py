# Que-write a python program given a list append and sort to do.
# solution-
numbers = [7,3,13,6,8,5,1,2,4,15,9,10,12,14,11]
list_1 = []
list_2 =[]

for num in numbers:
    if num < 6: 
        list_1.append(num) 
        list_1.sort() 

print(list_1)
print()