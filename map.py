# simpel function pass the parmeter in using the for loop condition 

# def cube(a):
#     return a*a*a

# l = [2,5,10,6]
# newL = []
# for item in l:
#     newL.append(cube(item))
# print(newL)


# map function using the system
def cube(a):
     return a*a*a

l = [2,5,10,6]

newL = list(map(cube,l))
print(newL)


# Filter function using the data mapping in condition based 
# Rules 1 other function def and pass the filter function direct way 
# Rules 2 not create def function in using the lambda function on filter direct way

# def filter_Function(a):
#      return a > 4

l = [2,5,10,6]

#newLIst = list(filter(filter_Function,l))
newLIst = list(filter(lambda a: a>4, l))
print(newLIst)


# Reduce function using the fisrt in import reqired 

from functools import reduce

Number = [1,2,5,6,10]

data = reduce(lambda x,y:x+y, Number)
print(data)

