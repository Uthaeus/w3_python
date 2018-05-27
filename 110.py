# Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.


def fifteens(l):
  result = []

  for x in l:
    if x % 15 == 0:
      result.append(x)

  print(result)



t1 = [3, 567, 543, 565, 150, 300]

fifteens(t1)


num_list = [45, 55, 60, 37, 100, 105, 220]
# use anonymous function to filter
result = list(filter(lambda x: (x % 15 == 0), num_list))
print("Numbers divisible by 15 are",result)