# Write a Python program to test whether a passed letter is a vowel or not.

def is_vowel(l):
  vowels = 'aeiou'
  user_l = l.lower()

  if user_l in vowels:
    result = f"{l} is a vowel"
  else:
    result = f"{l} is not a vowel"

  return result

user_in = input("Enter a letter: ")

print(is_vowel(user_in))
