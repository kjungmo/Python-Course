def calculator_plus(a, b):
 return int(a) + int(b)

def calculator_minus(a, b):
  return int(a) - int(b)

def calculator_times(a, b):
  return int(a) * int(b)

def calculator_division(a, b):
  return int(a) / int(b)

def calculator_negation(a):
  return -int(a)

def calculator_power(a, b):
  return pow(int(a), int(b)) 

def calculator_remainder(a, b):
  return int(a) % int(b)


print(calculator_plus(10, "20"))
print(calculator_minus(5, 4))
print(calculator_times(3, 4))
print(calculator_division(4, 2))
print(calculator_negation(400))
print(calculator_power(4, 2))
print(calculator_remainder(5, 2))