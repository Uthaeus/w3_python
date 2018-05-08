# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

def func(a, b):
  if a == b:
    return True 

  func_sum = a + b

  if a > b:
    func_dif = a - b
  else:
    func_dif = b - a

  if func_sum == 5 or func_dif == 5:
    return True 
  else:
    return False


print(func(3, 4))
print(func(4, 3))
print(func(4, 4))
print(func(2, 3))
print(func(3, 8))