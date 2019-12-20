age = 15

# if age >= 18:
#   print('Welcome to the dicotheque! you may come in')
# else:
#   print('you are too young, get out of here!')

age = 66
pension = 50000

if age <= 6:
  print('you must go to kindergarden')
elif age <= 17:
  print('you must go to school')
elif age < 65:
  print('you must go to work')
elif age > 65 or pension > 999999:
  print('you can retire')
else:
  print('you cannot retire because you dont have enough money in your pension')
