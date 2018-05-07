# Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]

def first_last(cl):
  first, *mid, last = cl 
  result = f"""
  first item: {first}\nlast item: {last}
  """
  print(result)

def find_items(cl):
  first = cl[0]
  last = cl[-1]
  result = "first item: " + first + "\nlast item: " + last 
  print(result)

color_list = ["Red","Green","White" ,"Black"]

first_last(color_list)
find_items(color_list)