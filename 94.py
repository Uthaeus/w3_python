# Write a Python program to convert a byte string to a list of integers.


def binar(s):
  new_str = s
  result = list(new_str)

  return result

test = b'This is a test'
test2 = 'This is a test'

print(binar(test))

def bin_iter(s):

  result_arr = []

  for x in s:
    result_arr.append(ord(x))

  return result_arr


print(bin_iter(test2))