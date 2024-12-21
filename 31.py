income = float(input("Enter your income: "))
credit_score = int(input("Enter your credit score: "))

if income > 50000:
    if credit_score > 700:
        print("Loan approved.")
    elif 600 <= credit_score <= 700:
        print("Loan approved with a higher interest rate.")
    else:
        print("Loan rejected.")
else:
    print("Loan rejected due to low income.")
