# Write a Python program to parse a string to Float or Integer.


def parser(s):
  float_str = float(s)
  int_str = int(float(s))

  print(float_str)
  print(int_str)


parser('324.678')
parser('435.23')