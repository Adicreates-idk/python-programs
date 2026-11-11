marks = (int(input("Enter the student's marks: ")))

if marks >= 93:
    grade = 'A'
elif marks >= 81:
    grade = 'B'
elif marks >= 71:
    grade = 'C'
elif marks >= 61:
    grade = 'D'
else:
    grade = 'Fail'

print(f"The student's grade is: {grade}")