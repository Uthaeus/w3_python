# Write a python program to sum of the first n positive integers.


def summer(l, n):
  result = 0
  count = 0

  temp = l[:n]

  for x in temp:
    result += x

  print(temp)
  print(result)

test = [1, 2, 3, 4, 5, 6]
test2 = [4, 5, 6, 1, 2, 3]

summer(test, 3)
summer(test2, 5)
