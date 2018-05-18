# Write a Python program to calculate midpoints of a line.


def midpoint(x1, y1, x2, y2):
  resx = (x1 + x2) / 2
  resy = (y1 + y2) / 2

  mid = f"Midpoint: ({resx}, {resy})"
  return mid


print('Coordinate Midpoint')
x_1 = float(input('Enter first X coordinate: '))
y_1 = float(input('Enter first y coordinate: '))
x_2 = float(input('Enter second x coordinate: '))
y_2 = float(input('Enter second y coordinate: '))

result = midpoint(x_1, y_1, x_2, y_2)

print(result)