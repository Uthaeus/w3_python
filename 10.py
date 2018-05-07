# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

def sum_num(n):
  output = f"{n} + {n}{n} + {n}{n}{n} = "
  answer = n + (n + n * 10) + (n + n * 10 + n * 100)

  print(output, answer)

user_in = int(input("Enter a number: "))

sum_num(user_in) 