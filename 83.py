# Write a Python program to test if a certain number is greater than all numbers of a list.


def greatest(l, n):
  new_list = sorted(l)
  return n > new_list[-1]

t1 = [2, 3, 4, 5, 6]
t2 = [12, 4, 2, 45, 65, 32, 3, 75, 6]

print(greatest(t1, 7))
print(greatest(t2, 100))

print(greatest(t1, 4))
print(greatest(t2, 14))

