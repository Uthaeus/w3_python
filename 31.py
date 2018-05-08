# Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
# Ex: gcd(54, 24) = 6

def gcd(num1, num2):
  larger_arr = []
  smaller_arr = []
  common = []

  if num1 > num2:
    smaller = num2
    larger = num1
  else:
    smaller = num1
    larger = num2

  for x in range(1, larger + 1):
    if larger % x == 0:
      larger_arr.append(x)

  for x in range(1, smaller + 1):
    if smaller % x == 0:
      smaller_arr.append(x)

  for x in smaller_arr:
    if x in larger_arr:
      common.append(x)

  result = common[-1]
  return f"The Greatest Common Denominator of {num1} and {num2} is:  {result}"


print(gcd(42, 56))

