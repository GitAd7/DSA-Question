# Calculating factorial

numb = int(input('Give the Number for Calculating Factorial: '))
if numb < 0:
    print('None')
elif numb == 0:
    print('The Factorial for 0 is 1')
else:
    result = 1
    while numb>0:
        result *= numb
        numb -= 1

print(f'The Factorial is: {result}')