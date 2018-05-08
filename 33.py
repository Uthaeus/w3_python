# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

def sum_of_three(a, b, c):

  if a == b or a == c or b == c:
    result = 0
  else:
    result = a + b + c 

  return result

print(sum_of_three(1, 2, 3))
print(sum_of_three(1, 2, 2))
print(sum_of_three(1, 1, 2))
print(sum_of_three(1, 2, 1))
print(sum_of_three(3, 3, 3))