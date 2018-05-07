#  Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.

def copies(s, n):
  if len(s) < 2:
    result = s * n 
  else:
    result = s[0: 2] * n 

  return result

user_in = input("Enter a string:\n")
times = int(input("How many times? "))

print(copies(user_in, times))