# Write a Python program to count the number 4 in a given list.

def four(l):
  count = 0
  user_list = []
  test_list = l.split(',')

  for x in test_list:
    user_list.append(int(x))

  for x in user_list:
    if x == 4:
      count += 1

  if count > 1:
    output = f"There are {count} 4's in your list"
  elif count == 1:
    output = "There is one 4 in your list"
  else:
    output = "There are no 4's in your list"

  return output


user_in = input("Enter some numbers:\n")

print(four(user_in))

