## Customizing Coffee

order = input('Please Specify Your Order:')
size = ['small','medium','large']
if order in size:
    ans = input('Would you like an extra shot of Espresso:')
    if ans == "Yes":
        print("I'll be right back with you coffee")
    else:
        print("I'll be back with your coffee")