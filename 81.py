# Write a Python program to concatenate N strings.


def concatter(*s):
  return ' '.join(s)


t1 = 'this is'
t2 = 'a test'
t3 = 'to see'
t4 = 'if this works'

print(concatter(t1, t2, t3, t4))