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
    
# This program prints a pattern of numbers based on the user input
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
    
# This program prints a pattern of numbers based on the user input
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()
    
# This program prints a pattern of stars based on the user input
for i in range(1,n+1):
    for j in range(n-i+1):
        print('* ',end="")
    print()
    
# This program prints a pattern of numbers based on the user input
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
  
 # This progrman print binary pattern based on the user input   
for i in range(1, n+1):
    start = 1 if i % 2 != 0 else 0
    for j in range(i):
        print(start,end=" ")
        start = 1-start
    print()
    
# This program prints a Number Crown Patterns based on the user input
for i in range(1,n+1):
    # Numbers
    for j in range(1, i+1):
        print(j,end=" ")
    # Space
    space = 2 * (n - i)
    for _ in range(1, space):
        print(' ', end="")
    # Numbers
    for j in range(i,0, -1):
        print(j,end=" ")
        space -=2
    print()

# This program prints a Increasing Number Triangle Patterns based on the user input
num = 1
for i in range(1,n+1):
    for j in range(i):
        print(num, end=" ")
        num = num+1
    print()
    
# This progrma prints Increasing Letter Triangle Patterns based on the user input
for i in range(n):
    for j in range(i+1):
        print(chr(ord('A')+j),end=" ")
    print()
    
# This program prints a Decreasing Letter Triangle Patterns based on the user input  
for i in range(n,0,-1):
    for j in range(i):
        print(chr(ord('A')+j),end=" ")
    print()
    
# This program prints a Alpha Ramp Patterns based on the user input
for i in range(1,n+1):
    c = chr(64+i)
    print((c+" ")*i)
    
# This program prints a Alpha Hill Patterns based on the user input
for i in range(1,n+1):
    # for spaces
    for j in range(1,(n-i)+1):
        print(" ",end="")
    # for char
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    for j in range(i-1,0,-1):
        print(chr(64+j),end=" ")
    # for spaces
    for j in range(1,(n-i)+1):
        print(" ",end="")
    print()
    
# This program prints a Alpha Triangle Patterns based on the user input
base = 65+n
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(base-j),end=" ")
    print()