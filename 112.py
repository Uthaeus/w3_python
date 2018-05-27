# Write a Python program to remove the first item from a specified list.


def first(l):
  first_item = l[0]
  new_list = l[1:]

  print(first_item)
  print(new_list)

  del l[0]
  print(l)


t1 = [1, 2, 3, 4, 5]

first(t1)
