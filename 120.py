# Write a Python program to format a specified string to limit the number of characters to 6.


def limiter(s):
  if len(s) <= 3:
    result = s + '...'
  elif len(s) > 3 and len(s) <= 6:
    result = s[0:3] + '...'
  else:
    result = s[0:6] + '...'

  return result


t1 = 'this is a test'
t2 = 'this'
t3 = 'hi'


print(limiter(t1))
print(limiter(t2))
print(limiter(t3))
