## Keep asking the user for input until they enter a number between 1 and 10.

while True:
    try:
        number = int(input("Enter a number between 1 and 10: "))
        if number >= 1 and number <= 10:
            print("Welcome in the Dungeon!")
            break
        else:
            print("Please enter a number between 1 and 10 to Enter Into the Dungeon")
    except ValueError:
        print("Please enter a number between 1 and 10 to Enter Into the Dungeon")
        