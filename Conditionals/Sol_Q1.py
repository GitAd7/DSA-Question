## Age Group Categorisation

age = int(input("Enter your Age:",))
if age<13:
    print('You are a Child!, Entry is free')
elif 13<=age<=19:
    print("You are a Teenager!, The Entry Fee is 5 rupees")
elif 20<=age<=59:
    print("You are an Adult!, Entry Fee is 10 rupees")
elif age>59:
    print("You are a Senior Citizen!, The Entry Fee is 10 rupees")
else:
    print("Entry is Not Allowed!")
