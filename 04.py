# Write a Python program which accepts the radius of a circle from the user and compute the area.
from math import pi
# A=πr2

def calc_area(r):
  return pi * (r ** 2)

print("Let's find a circle's area")

radius = float(input("Enter your circle's radius: "))

result = calc_area(radius)

output = f"The area of a circle with a radius of {radius} is: {result}."

print(output)