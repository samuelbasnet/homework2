score = float(input("Enter your subject score: "))

if score > 90:
    print("Congratulations!")
elif 50 <= score <= 90:
    print("You can improve.")
else:
    print("Please retake the course.")
