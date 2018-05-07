# Write a Python program to test whether a number is within 100 of 1000 or 2000.

def within_hundred(num):
  if num >= 900 and num <= 1100:
    print("Your number is within 100 of 1000")
  elif num >= 1900 and num <= 2100:
    print("Your number is within 100 of 2000")
  else:
    print("Your number is not within 100")


user_in = int(input("Enter a number: "))

within_hundred(user_in)