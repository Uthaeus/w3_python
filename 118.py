# Write a Python program to create a bytearray from a list


def byter(l):
  byte_list = bytearray(l)

  for x in byte_list:
    print(x)


t1 = [1, 2, 3, 4, 5]

byter(t1)


print()
nums = [10, 20, 56, 35, 17, 99]
# Create bytearray from list of integers.
values = bytearray(nums)
for x in values: print(x)
print()
