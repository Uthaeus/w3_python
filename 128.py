# Write a Python program to check if lowercase letters exist in a string.


def is_lower(s):
  count = 0

  for x in s:
    if ord(x) >= 97 and ord(x) <= 122:
      count += 1

  if count > 0:
    result = f"There are {count} lowercase letters"
  else:
    result = "There are no lowercase letters"

  return result


t1 = 'This is a test'
t2 = 'THIS IS A TEST'
t3 = 'THIS IS a TEST'

print(is_lower(t1))
print(is_lower(t2))
print(is_lower(t3))

print(any(c.islower() for c in t1))
print(any(c.islower() for c in t2))
print(any(c.islower() for c in t3))
