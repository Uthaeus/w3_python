# Write a Python program to display your details like name, age, address in three different lines.

def info(n, age, add):
  result = f"""
  Name: {n}\nAge: {age}\nAddress: {add}
  """
  result2 = f"Name: {n}\nAge: {age}\nAddress: {add}"
  print(result)
  print(result2)


user_n = input("Enter your name: ")
user_age = input("Enter your age: ")
user_add = input("Enter your address: ")

info(user_n, user_age, user_add)
