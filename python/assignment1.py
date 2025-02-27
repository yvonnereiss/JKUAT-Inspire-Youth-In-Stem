# Ask the user for their exam score
score = int(input("Enter your exam score (0 - 100):"))

# Determine the grade based on the score
if 90 <= score <= 100:
    grade = "A"
elif 80 <= score <= 89:
    grade = "B"
elif 70 <= score <= 79:
    grade = "C"
elif 60 <= score <= 69:
    grade = "D"
elif 50 <= score <= 59:
    grade = "E"
elif 0 <= score <= 49:
    grade = "F"
else:
    grade = "Invalid score"

# Output the result
print(f"Your grade is: {grade}")