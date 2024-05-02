## Counting Positive Occurence

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
pos_count = 0
for i in numbers:
    if i>0:
        pos_count += 1
print(f'Total Number of Positive Occurence is {pos_count}')