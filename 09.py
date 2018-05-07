# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

def exam_date(tup):
  a, b, c = tup
  result = f"{a} / {b} / {c}"
  return result

exam_st_date = (11, 12, 2014)
answer = exam_date(exam_st_date)

print(f"The examination will start: {answer}")
