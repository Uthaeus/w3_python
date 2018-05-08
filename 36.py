# Write a Python program to add two objects if both objects are an integer type.

def type_check(a, b):
  if isinstance(a, int) and isinstance(b, int):
    result = a + b 
  else:
    result = "Need two numbers"
  return result


print(type_check(3, 4))
print(type_check('a', 3))
print(type_check('a', 'b'))
print(type_check(3, 3))