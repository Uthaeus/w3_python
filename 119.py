# Write a Python program to display a floating number in specified numbers


def rounder(n):
  return round(n, 2)


user = float(input('Enter a value: '))

result = f"You entered {rounder(user)}"

print(result)

