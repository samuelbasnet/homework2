salary = float(input("Enter the salary: "))
service_years = int(input("Enter the number of years of service: "))

if service_years > 5:
    bonus = salary * 0.05
else:
    bonus = 0

print(f"The net bonus amount is Rs {bonus:.2f}.")
