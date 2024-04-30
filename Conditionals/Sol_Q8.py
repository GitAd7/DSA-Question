## Password Strenght Checker

password = input('Please Write your Password here: ')
if len(password)<6:
    print("Your Password Strenght is: Weak")
elif 6<len(password)<10:
    print("Your Password Strenght is: Medium")
elif len(password)>10:
    print("Your Password Strenght is: Strong")
else:
    print("Just Don't do it!")