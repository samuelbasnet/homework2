grade = int(input("Enter the grade: "))

if grade < 25:
    result = "D"
elif grade < 45:
    result = "C"
elif grade < 50:
    result = "B"
elif grade < 60:
    result = "B+"
elif grade <= 80:
    result = "A"
else:
    result = "A+"

print(f"The grade is {result}.")
