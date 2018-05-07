# Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.


def sum_nums(a, b, c):
  if a == b and b == c:
    ans = (a * 3) * 3
  else:
    ans = a + b + c 

  return ans


num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))

print(sum_nums(num1, num2, num3))
