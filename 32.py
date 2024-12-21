weather = input("Enter the weather (sunny/rainy): ").lower()

if weather == "sunny":
    print("You can go hiking or have a picnic.")
elif weather == "rainy":
    raincoat = input("Do you have a raincoat or umbrella? (yes/no): ").lower()
    if raincoat == "yes":
        print("You can go to a nearby mall or museum.")
    else:
        print("You should stay home and watch movies.")
else:
    print("Invalid weather input.")
