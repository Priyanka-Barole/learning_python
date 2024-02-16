# Que - Let’s say I give you a list saved in a variable: years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]. Write one line of Python that takes this list a and makes a new list that has only the [24, 23, 24, 24, 22, 23].of this list in it.
# solution-

years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
ages = []
for year in years_of_birth: 
  ages.append(2014 - year)

years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
ages = [2014 - year for year in years_of_birth]
print(ages)