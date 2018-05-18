# Write a Python program to calculate the hypotenuse of a right angled triangle.


def hypot(a, b):
  result = ((a ** 2) + (b ** 2)) ** 0.5
  return result

print('Hypotenuse Calculator')
first = float(input('Enter first side: '))
second = float(input('Enter second side: '))

ans = hypot(first, second)

print(f'A right triangle with sides of {first} and {second} has a hypotenuse of: {ans}')