# Write a Python program to solve (x + y) * (x + y).
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49

def mather(x, y):
  template = "(x + y) * (x + y)"
  result1 = f"x = {x}, y = {y}\n({x} + {y}) * ({x} + {y})"
  result2 = (x + y) ** 2
  result3 = f"({x} + {y}) ^ 2 = {result2}"

  print(template)
  print(result1)
  print(result3)

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

mather(num1, num2)
