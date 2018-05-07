# Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.


def add_is(s):
  beg = s[0:2]
  if beg == "Is":
    return s 
  else:
    return "Is " + s.lower() 

user_in = input("Enter a string\n")

print(add_is(user_in))
