total_days = int(input("Enter total number of days: "))
absent_days = int(input("Enter total number of absent days: "))

attendance_percentage = ((total_days - absent_days) / total_days) * 100

if attendance_percentage < 75:
    print("You will not be able to sit in the exam.")
else:
    print(f"Your attendance percentage is {attendance_percentage:.2f}%.")
