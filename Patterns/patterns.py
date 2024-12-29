n = int(input("Enter the number of rows: "))
# This program prints a square pattern of stars based on the user input
for i in range(n):
    for j in range(n):
        print('*', end='')
    print()
    
# This program prints a right-angled triangle pattern of stars based on the user input
for i in range(n):
    for j in range(i+1):
        print('* ',end="")
    print()
    
# This program prints a right-angled triangle pattern of numbers based on the user input
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
    
# This program prints a right-angled triangle pattern of numbers based on the user input
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()
    
# This program prints a right-angled triangle pattern of stars based on the user input
for i in range(1,n+1):
    for j in range(n-i+1):
        print('* ',end="")
    print()
    
# This program prints a right-angled triangle pattern of numbers based on the user input
for i in range(n):
    for j in range(1,n-i+1):
        print(j, end=" ")
    print()
    
# This program prints a star pattern based on the user input
for i in range(n):
    # For Spaces
    for j in range(n-i-1):
        print(' ',end="")
    # for stars
    for j in range(2*i+1):
        print('*',end="")
    # for spaces
    for j in range(n-i-1):
        print(' ',end="")
    print()
    
# This program prints a Inverse Star pattern based on the user input
for i in range(n):
    # For Spaces
    for j in range(i):
        print(' ',end="")
    # For Stars
    for j in range(2*n-(2*i+1)):
        print('*',end="")
    # For Spaces
    for j in range(i):
        print(' ',end="")
    print()
    
# This program prints a rotated triangle pattern of stars based on the user input
for i in range(1,2*n):
    stars = i
    if i > n: stars= 2*n-i
    for j in range(stars):
        print('*',end="")
    print()