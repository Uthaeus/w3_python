# Write a Python program to swap two variables.


def swapper(a, b):
  print(a)
  print(b)
  print('****')
  a, b = b, a
  print(a)
  print(b)


first = 1
second = 2

swapper(first, second)