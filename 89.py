# Write a Python program to perform an action if a condition is true.


def if_first(v):
  if v == 1:
    print('First day of the month')
  else:
    print('I was instructed not to mention...')


user = int(input('Enter a value: '))
if_first(user)
