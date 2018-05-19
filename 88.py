# Given variables x=30 and y=20, write a Python program to print t "30+20=50".


def calculation(n1, n2):
  result = f"{n1} + {n2} = {n1 + n2}"

  print(result)


num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
calculation(num1, num2)