# Write a Python program to display the current date and time.

import datetime

def get_time():
  now = datetime.datetime.now()
  print("Current date and time:")
  print(now.strftime("%Y-%m-%d %H:%M:%S"))


get_time()