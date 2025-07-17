n = int(input("Enter the number of students: "))
students = []

for i in range(n):
    name = input("Enter student name: ")
    score = float(input("Enter the score: "))
    students.append([name, score])

# Extract unique, sorted grades
unique_grades = sorted(set(student[1] for student in students))

# Get second lowest grade
second_lowest_grade = unique_grades[1]

# Get names with second lowest grade, sorted alphabetically
result = sorted([student[0] for student in students if student[1] == second_lowest_grade])

# Output the result
for name in result:
    print(name)
