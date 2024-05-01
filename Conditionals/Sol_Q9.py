## Leap Year

year = int (input("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0):
    print(f'{year} is the leap year')
else:
    print(f'{year} is not the leap year')