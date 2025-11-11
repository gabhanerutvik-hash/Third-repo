import random
print("Welcome to lucky number contest")
while True:
    choice = input("press 'Enter' to play the game and q to 'Quit'")
    choice = choice.strip()
    if choice == 'q':
        print("Thanks for participation ,Goodbye")
        break
    print("please purchase the token to play the game")
    number = input("Enter a number from 1 to 20")
    if number == '10':
        print("Congrats you have just win a lottery prize of $10,000,000")
        break
    else:
        print("Sorry you just lose the game , better luck next time")
