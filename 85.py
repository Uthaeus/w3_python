#  Write a Python program to check if a file path is a file or a directory.


import os  


# path="abc.txt"  
# if os.path.isdir(path):  
#     print("\nIt is a directory")  
# elif os.path.isfile(path):  
#     print("\nIt is a normal file")  
# else:  
#     print("It is a special file (socket, FIFO, device file)" )
# print()


def define_path(f):
  if os.path.isdir(f):
    print('This is a directory')
  elif os.path.isfile(f):
    print('This is a file')
  else:
    print('This is a special file')

user = input('Enter a file or path to test:\n')
define_path(user)