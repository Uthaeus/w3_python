# Write a Python program to get the size of a file.


import os


def get_size(f):
  return os.path.getsize(f)


user = input('Enter file name to see size: ')
print(get_size(user))