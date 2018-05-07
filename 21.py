# Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

def even_odd(n):
  if n % 2 == 0:
    print("Your number is even")
  else:
    print("Your number is odd")

user_in = int(input("Enter a number: "))

even_odd(user_in)