# Student Grading Automation

name = input("Enter Student Name: ")
num_subjects = int(input("Enter number of subjects: "))

total_marks = 0
for i in range(1, num_subjects + 1):
    marks = float(input(f"Enter marks for subject {i}: "))
    total_marks += marks

average = total_marks / num_subjects

if average >= 90:
    grade = 'A'
elif average >= 75:
    grade = 'B'
elif average >= 50:
    grade = 'C'
else:
    grade = 'Fail'

print("\n--------STUDENT RESULTS--------\n")
print(f"Name: {name}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average}")
print(f"Grade: {grade}")