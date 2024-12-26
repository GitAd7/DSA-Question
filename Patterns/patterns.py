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