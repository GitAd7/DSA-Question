## Sum of Even Numbers

n = int(input("Insert Number of your choice: "))
sum = 0
for i in range(0, n+1, 2):
    sum += i
print(f'Sum of Even Number upto {n} is {sum}') 