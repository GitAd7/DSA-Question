# Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate
items = str(input("Enter the string to check duplicate:"))
count = 0
for i in (items):
    if items.count(i) > 1:
        print(f"Duplicate found: {i}")
        count = +1
        break
if count ==0:
    print('No duplicates found in string')