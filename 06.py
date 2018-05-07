# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

nums = input("Enter some numbers:\n")

num_list = nums.split()
num_tuple = tuple(num_list)

print(num_list)
print(num_tuple)