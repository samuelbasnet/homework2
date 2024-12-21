service_years = int(input("Enter the number of years of service: "))
salary = float(input("Enter the salary: "))

if service_years > 10:
    bonus = salary * 0.10
elif 6 <= service_years <= 10:
    bonus = salary * 0.08
else:
    bonus = salary * 0.05

print(f"The bonus amount is Rs {bonus:.2f}.")
