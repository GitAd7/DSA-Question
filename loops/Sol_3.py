# Printing Multiplication Table

n = int(input('Enter your desired number: '))
for i in range(1,11):
    if i == 5:
        continue
    print(f"{n} x {i} = {n*i}")
        