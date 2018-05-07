# Write a Python program to get a string which is n (non-negative integer) copies of a given string.

def copy_str(s, n):
  x = 0
  while x < n:
    print(s)
    x += 1


user_in = input("Enter a string\n")
times = int(input("How many times? "))

copy_str(user_in, times)
