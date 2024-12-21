print("Welcome to the Space Mission!")
choice1 = input("Do you want to go to the moon or to Mars? ").lower()

if choice1 == "to mars":
    print("Game Over")
elif choice1 == "to the moon":
    choice2 = input("Do you want to land on the surface or stay in orbit? ").lower()
    if choice2 == "land on the surface":
        print("Game Over")
    elif choice2 == "stay in orbit":
        choice3 = input("Choose between alien, asteroid, or satellite: ").lower()
        if choice3 == "alien" or choice3 == "asteroid":
            print("Game Over")
        elif choice3 == "satellite":
            print("You Win")
        else:
            print("Invalid choice.")
else:
    print("Invalid choice.")
