## Reversing String

any = str(input("Give Your Desired String: "))
rev_str = ""
for char in any:
    rev_str = char + rev_str

print(f'Reverse of Desired string is: {rev_str}')