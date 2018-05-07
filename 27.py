# Write a Python program to concatenate all elements in a list into a string and return it.

def concatter(l):
  form_list = l.split(',')
  result = "".join(form_list)
  print(l)
  print(form_list)
  print(result)

user_in = input("Enter a list of words:\n")

concatter(user_in)

print("test".split())