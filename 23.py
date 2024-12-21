age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()

if 18 <= age < 30:
    wage = 700 if gender == "M" else 750
elif 30 <= age <= 40:
    wage = 800 if gender == "M" else 850
else:
    wage = "No wage available for this age group."

print(f"Your wage per day is {wage}.")
