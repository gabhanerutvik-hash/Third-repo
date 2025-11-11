import random
print("Welcome to the Rolling Dice Game!")
while True:
 choice = input("press 'Enter' to play the game and q to 'Quit'")
 if choice=='q':
    print("Thanks for playing the game ,Goodbye!")
    break
 elif choice=='':
    number=random.randint(1,6)
    print("You rolled a ",number)
 else:
    print("Please enter valid input")
