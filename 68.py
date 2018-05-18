# Write a Python program to calculate the sum of the digits in an integer.


def summer(n):
  new_str = str(n)
  str_arr = []
  result = 0

  for x in new_str:
    str_arr.append(int(x))

  for x in str_arr:
    result += x


  print(result)


summer(123)
print('********')
summer(456)
