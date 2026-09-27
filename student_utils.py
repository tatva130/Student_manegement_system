import validation 


def display_students(students):
    return [student for student in students]


def find_top_student(students):
    return max(students, key=lambda x: x["cgpa"]) 

def find_student(students):
    name = input("Enter student name: ")

    for student in students:
        if student["name"] == name:
            return student
    return None


def find_by_skill(students):
    skill = input("Enter a skill: ")

    return [student for student in students if skill in student["skills"]] 


def calculate_average_cgpa(students):
    return sum(s["cgpa"] for s in students) / len(students) 


def add_student(students):
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    cgpa = float(input("Enter student CGPA: "))
    skill = input("Enter student skill: ")

    student = { "name": name,
                "age": age,
                "cgpa": cgpa, 
                "skills": skill.split(",")
             }

    students.append(student)

    return "\nStudent added successfully."


def remove_student(students):
    name = input("Enter student name: ")

    for student in students:
        if student["name"] == name:
            students.remove(student)
            return "\nStudent removed successfully."