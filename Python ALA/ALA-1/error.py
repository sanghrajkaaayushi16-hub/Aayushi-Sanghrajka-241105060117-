print("Student Rank System")
students = int(input("Enter student count: "))
i = 0
highest = 0
total = 0
while i < students:
marks = int(input("Enter marks: "))
total = total + marks
if marks > highest:
highest = marks
if marks >= 90:
print("Grade A")
elif marks >= 75:
print("Grade B")
elif marks >= 50:
print("Grade C")
else
print("Fail")
i = i + 1
average = total / students
print("Highest:", highest)
print("Average:", average
if average > 80:
print("Top Class")
else:
print("Normal Class")