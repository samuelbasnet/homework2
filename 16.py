N = int(input("Enter the number of students: "))
K = int(input("Enter the number of apples: "))

apples_per_student = K // N
remaining_apples = K % N

print(f"Each student gets {apples_per_student} apples.")
print(f"{remaining_apples} apples remain in the basket.")
