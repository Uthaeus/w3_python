# Write a Python program to accept a filename from the user and print the extension of that.

def get_ext(f):
  f_list = f.split(".")
  ext = f_list[-1]
  return ext 

user_file = input("Enter your filename:\n")

result = get_ext(user_file)

print(f"Your extension is .{result}")