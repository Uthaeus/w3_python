# Write a Python program to filter the positive numbers from a list.


def evens(l):

  result = list(filter(lambda x: (x % 2 == 0), l))

  return result 

t1 = [1, 2, 3, 4, 5, 6, 7, 8]


print(evens(t1))