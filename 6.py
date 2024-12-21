subject1=int(input("Enter your subject1 marks: "))
subject2=int(input("Enter your subject2 marks here: "))
subject3=int(input("Enter your subject3 marks here: "))
subject4=int(input("Enter your subject4 marks here: "))
total_marks=subject3+subject2+subject4+subject1
print(f"The total marks is {total_marks}")
percentage=(total_marks/400)*100
print(f"The percentage is {percentage}%")
if percentage>70:
    print("distinction")
elif percentage>60 and percentage<70:
    print("First")
elif percentage>40 and percentage<60:
    print("pass")
else:
    print("Fail")