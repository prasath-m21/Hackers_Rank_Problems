
n = int(input("Enter number of students: "))
student_marks = {}
for _ in range(n):
    parts = input().split()
    name = parts[0]
    scores = list(map(float, parts[1:]))
    student_marks[name] = scores
query_name = input("Enter student name: ")
avg = sum(student_marks[query_name]) / len(student_marks[query_name])
print(f"{avg:.2f}")
