class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Test the function with a list of students
students = [
    Student("Priya", "01", 3.0),
    Student("Tina", "02", 4.0),
    Student("Madhu", "03", 4.9),
    Student("Deepa", "04", 3.5),
]

sorted_students = sort_students(students)


for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")