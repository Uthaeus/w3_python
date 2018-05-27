# Write a Python program to compute the product of a list of integers (without using for loop)

from functools import reduce


def product(l):
  x = 0
  result = 1

  while x < len(l):
    result *= l[x]
    x += 1

  return result

t1 = [1, 2, 3, 4, 5]

print(product(t1))


def reducer(l):

  result = reduce((lambda x, y: x * y), l)

  return result


print(reducer(t1))