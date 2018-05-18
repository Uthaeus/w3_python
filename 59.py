# Write a Python program to convert height (in feet and inches) to centimeters.
# 1 in = 2.54 cm


def converter(f, i):
  total_inches = (f * 12) + i 

  cms = total_inches * 2.54

  output = f"{cms}cm"

  return output 


# print(converter(3, 6))

print('**************')
print('Welcome to height converter')

feet = int(input("Enter number of feet: "))
inches = int(input("Enter number of inches: "))

result = converter(feet, inches)
print(result)