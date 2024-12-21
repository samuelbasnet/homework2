from inspect import walktree

print("Welcome to Treasure Land")
user_choice=input("Choose a direction: ")
if user_choice=="right":
    print("Game Over")

elif user_choice=="left":
    user_choice=input("choose your desired activity: ")
    if user_choice=="swim":
        print("Game over")
    elif user_choice=="walk":
        user_choice=input("choose your color: ")
        if user_choice=="red" or user_choice=="blue":
            print("Game Over")
        else:
            print("you win")


