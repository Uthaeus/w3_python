# Write a Python program to create a histogram from a given list of integers.

def histogram(l):
  li = map(int, l.split(','))


  for x in li:
    output = ""
    times = x
    while(times > 0):
      output += '*'
      times -= 1
    print(output)


test = [2, 3, 6, 5]
histogram(test)

user_in = input("Enter some numbers:\n")

histogram(user_in)