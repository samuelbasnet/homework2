num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print(f"The greater number is {num1}.")
elif num2 > num1:
    print(f"The greater number is {num2}.")
else:
    if num1 > 0:
        print("Both numbers are equal and positive.")
    elif num1 < 0:
        print("Both numbers are equal and negative.")
    else:
        print("Both numbers are zero.")
