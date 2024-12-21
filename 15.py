a = int(input("Enter the number of students in class 1: "))
b = int(input("Enter the number of students in class 2: "))
c = int(input("Enter the number of students in class 3: "))

desks = (a + 1) // 2 + (b + 1) // 2 + (c + 1) // 2

print(f"The minimum number of desks required is {desks}.")
