# Write a Python program to check if a string is numeric.



def is_number(s):
  if s[0] in ('-', '+'):
    return s[1:].isdigit()
  else:
    return s.isdigit()


test1 = '123'
test2 = 'abc'
test3 = 'a1b2'
test4 = '-23'

print(is_number(test1))
print(is_number(test2))
print(is_number(test3))
print(is_number(test4))