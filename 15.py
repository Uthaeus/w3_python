# Write a Python program to get the volume of a sphere with radius 6.

# V = 4/3πr3

from math import pi

def sphere_vol(r):
  return (4/3) * pi * (r ** 3)

radius = int(input("What is your sphere's radius? "))

answer = f"A sphere with a radius of {radius} has a volume of: "
result = sphere_vol(radius)

print(answer, result)