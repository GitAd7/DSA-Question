## Movie Ticket Pricing

age = int(input('Enter Your Age Please:',))
day = str(input("Enter Today's Day:",))
if day == "Wednesday":
    if age<18:
        print("The Price of ticket is $6. Thanks for watching with us!")
    else:
        print("The Price of Ticket is $10. Thanks for Watching with us!")
else:
    if age<18:
        print("The Price of ticket is $8. Thanks for watching with us!")
    else:
        print("The Price of Ticket is $12, Thanks for watching with us!")