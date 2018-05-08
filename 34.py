# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

def summer(a, b):
  result = a + b

  if result >= 15 and result <= 20:
    result = 20

  return result

print(summer(5, 5))
print(summer(10, 6))
print(summer(10, 11))