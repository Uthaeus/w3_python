# Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure

# 1 kilopascal = 0.145 psi
# 1 kilopascal = 0.00987 atm
# 1 kilopascal = 7.5 mmHg

def converter(p):
  psi = p * 0.145
  mmhg = p * 7.5
  atm = round(p * 0.00987, 5)

  result = f"psi: {psi}\nmmHg: {mmhg}\natm: {atm}"
  return result

print('Pressure Converter')
press = float(input('Enter pressure in kilopascals: '))

print(converter(press))
