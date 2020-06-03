import random
#       [expression for variable in expression]
list = [num for num in range(100000)]
#  we can also try this
odd = [i for i in list if i%2 is not 0]
even = [i for i in list if i%2 is 0]
print(min(list))
print(max(list))