# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

def seventeen(n):
  if n > 17:
    result = (n - 17) * 2
  elif n <= 17:
    result = 17 - n 

  return result


user_in = int(input("Enter a number greater than 0\n"))

print(seventeen(user_in))

