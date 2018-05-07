# Write a Python program to check whether a specified value is contained in a group of values.

# Test Data : 
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

def num_check(l, n):
  li = []
  for x in l:
    li.append(int(x))

  if n in li:
    return True
  else:
    return False

test_list = [1, 5, 8, 3]
test_num1 = 3
test_num2 = -1

print("test 1", num_check(test_list, test_num1))
print("test 2", num_check(test_list, test_num2))

user_list = input("Enter a list of numbers:\n")
user_num = int(input("Enter a number to check for: "))

print(num_check(user_list, user_num))
