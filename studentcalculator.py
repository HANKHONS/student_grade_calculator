
def Gradecalculator(students):
    """Calculate grades for students based on their marks."""
    print("Welcome to the Student Grade Calculator")
    for student, info in students.items():
        mark = info["marks"]
        if mark < 30:
            students[student]["grade"] = "F"
        elif mark >= 30 and mark < 50:
            students[student]["grade"] = "D"
        elif mark >= 50 and mark < 60:
            students[student]["grade"] = "C"
        elif mark >= 60 and mark < 70:
            students[student]["grade"] = "B"
        elif mark >= 70 and mark < 80:
            students[student]["grade"] = "A"
        elif mark >= 80:
            students[student]["grade"] = "A+"
    return students


students = {
    "student 1": {"name": "John", "marks": 85},
    "student 2": {"name": "Alice", "marks": 72},
    "student 3": {"name": "Bob", "marks": 45},
}

result = Gradecalculator(students)

passing_students = [info["name"] for info in result.values() if info["grade"] != "F"]

top_performers = [info["name"] for info in result.values() if info["grade"] == "A+"]

for student, info in result.items():
    print(f'{info["name"]} : {info["marks"]} marks ---> Grade {info["grade"]}')

print(f"Passed The course: {passing_students}")
print(f"Top Performers: {top_performers}")
