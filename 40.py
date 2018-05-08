# Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

import math

def get_distance(a, b):
  result = math.sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2))

  return result

p1 = [4, 0]
p2 = [6, 6]

print(get_distance(p1, p2))
