# ask for age 
age = input('How old are you?: ')
age = int(age)
if age >= 18 and int(age) < 21:
  # 18-21 wristband
  print('You can enter, but need a wristband!')
elif age >= 21:
  # 21+ drink, normal entry
  print('you are good to enter and can drink!')
else:
  # too young, sorry
  print('You cant come in, little one!')




