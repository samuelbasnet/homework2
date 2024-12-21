percentage = float(input("Enter your percentage: "))

if percentage < 40:
    category = "Failed"
elif percentage < 55:
    category = "Fair"
elif percentage < 65:
    category = "Good"
elif percentage >= 65:
    category = "Excellent"

print(f"Your category is {category}.")
