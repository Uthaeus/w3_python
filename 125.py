# Write a Python program to sum of all counts in a collections?

from functools import reduce

def counter(d):
  result = []

  for x in d:
    result.append(d[x])

  return reduce((lambda x, y: x + y), result)



 
t1 = {'a': 1, 'b': 2, 'c': 1, 'd': 4}

print(counter(t1))