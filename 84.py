# Write a Python program to count the number occurrence of a specific character in a string.


def character_count(s, c):
  count = 0

  for x in s:
    if x == c:
      count += 1

  result = f"For character {c}: {count}"
  return result


t1 = 'This is a test'
t2 = 'Another test to see count of e'

print(character_count(t1, 't'))
print(character_count(t2, 'e'))


def char_count(s, c):
  # count = s.count(c)

  result = f"Character {c} appears {s.count(c)} times."
  return result


print(char_count(t1, 't'))
print(char_count(t2, 'e'))
