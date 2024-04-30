## Fruit Ripeness Checker

color = input(print('Please Specify the color of fruit:'))
if color == 'Green':
    print('Fruit is Unripe, please wait for few hours before eating')
elif color == "Yellow" or "Red":
    print('The fruit is riped, you can eat any time you want.')
elif color == "Brown":
    print('The fruit is Overripe, it is advised to not eat it.')
else:
    print('Please Specify the colors for Mango, Apple, or Banana')