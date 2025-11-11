import random
print("Welcome to 'spin the wheel'")
while True:
    choice = input("press 'Enter' to play the game and q to 'Quit'")
    choice = choice.strip()
    if choice =='q':
        print("Thanks for spinning the wheel ,Goodbye")
        break
    spin = random.choice(["None", "Tv", "Refrigerator", "Laptop", "Mackbook"])
    if spin == "None":
        print("Sorry,you did not win anything.Better luck next time.")
        break
    elif choice == '':
        print(f"You rolled to {spin}")
        print("Congrats !!You have just win a ",{spin})
