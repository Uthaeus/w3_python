# Write a Python program to convert the distance (in feet) to inches, yards, and miles.


def converter(f):
  inches = f * 12
  yards = f / 3
  miles = f / 5280

  result = f"{f} feet:\n{inches} inches\n{yards} yards\n{miles} miles"

  return result


print("**Feet converter**")
feet = float(input("Enter number of feet: "))

print(converter(feet))