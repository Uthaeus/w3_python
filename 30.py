# Write a Python program that will accept the base and height of a triangle and compute the area.

# A = 1/2 * (b * h)

def tri_area(b, h):
  return (1 / 2) * (b * h)


base = int(input("What is the base size of your triangle? "))
height = int(input("What is the height of your triangle? "))
area = tri_area(base, height)

print(f"A triangle with a base of {base} and a height of {height} has an area of: {area}")