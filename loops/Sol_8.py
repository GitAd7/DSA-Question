# Check if a number is prime
numb = int(input('Enter the number you want to check for prime:'))
count = 0
for i in range(2, numb):
    if numb % i == 0:
        print('Your Number is not prime')
        count += 1
        break
    if count == 0:
        print(f'{numb} is prime')