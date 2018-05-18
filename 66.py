# Write a Python program to calculate body mass index.


# Body Mass Index is a simple calculation using a person's height and weight. The formula is BMI = kg/m2 where kg is a person's weight in kilograms and m2 is their height in metres squared. A BMI of 25.0 or more is overweight, while the healthy range is 18.5 to 24.9.
# 1 pound (lb) is equal to 0.45359237 kilograms (kg).
# 1 inch is equal to 0.0254 meters

def calculator(w, f, i):
  kgs = w * 0.45359237
  h = (f * 12) + i 
  mtrs = h * 0.0254

  bmi = kgs / (mtrs ** 2)

  return bmi


print('Body Mass Index')
weight = float(input('First: Please enter your weight in pounds: '))
feet = float(input('Next, height: Please enter number of feet: '))
inches = float(input('Now the number of inches: '))

result = round(calculator(weight, feet, inches), 2)

if result < 18:
  print('Looks like you could stand to gain a few lbs.')
  print(result)
elif result >= 18 and result <= 24.9:
  print('You are within recommended parameters')
  print(result)
elif result > 24.9:
  print('You may want to try a workout regimine')
  print(result)


