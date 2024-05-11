# First Non-Repeated Character

any = str(input("Specify the string of Your Choice: "))
count = {}
for char in any:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
        
for char in any:
    if count[char] == 1:
        desired_char = char
        
print(f'The first Non-Repeatted Char in Given String is: {desired_char}')