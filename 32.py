# Write a Python program to get the least common multiple (LCM) of two positive integers.

def lcm(num1, num2):
  smaller_list = []
  larger_list = []
  common = []

  if num1 > num2:
    larger = num1
    smaller = num2
  else:
    larger = num2
    smaller = num1

  combined = larger * smaller 

  for x in range(1, combined + 1):
    smaller_list.append(smaller * x)
    larger_list.append(larger * x)

  for x in smaller_list:
    if x in larger_list:
      common.append(x)

  result = common[0]

  return f"The Least Common Multiple of {num1} and {num2} is:  {result}"

print(lcm(4, 6))