# Write a Python program to get the Python version you are using.

import sys

def get_version():
  print("Python version:")
  print(sys.version)
  print("Version info:")
  print(sys.version_info)

get_version()