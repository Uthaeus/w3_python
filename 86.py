# Write a Python program to get the ASCII value of a character.


def get_ascii(c):
  return ord(c)


user = input('Enter character: ')
print(get_ascii(user))