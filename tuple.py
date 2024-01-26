# cheak Tuple type
colours=("blue","gree","rad")
print(type(colours))
# cheak Tuple lenth
colours=("blue","gree","rad")
print(len(colours))'''
'''colours=("blue","gree","rad")
colours=tuple(("blue"))
#accessing items in tuple
colours=("blue","gree","rad")
print(colours[1])
print(colours[-1])
print(colours[1:3])
print(colours[-2:])
#check if an itme exists in tuple
if "gree" in colours:
	print("gree is part of tuple")
# concatenate 2 tuples
more_colours=("green","yellow")
colours = colours+more_colours
print(colours)	
# unpacking a tuple 
colour1,colour2,colour3=colours
print(colour1,colour2,colour3)

input_tuple=(1,2,3,4,5,6)
lst=[]
for x in reversed(input_tuple):
	lst.append(x)
	output_tuple=tuple(lst)
	print(output_tuple)
