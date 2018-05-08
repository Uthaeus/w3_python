# Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years. Go to the editor
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79

def future(amt, inter, yrs):
  interest = inter / 100
  for x in range(1, yrs + 1):
    amt += (amt * interest)

  return round(amt, 2) 

print(future(10000, 3.5, 7))