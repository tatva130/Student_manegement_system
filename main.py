import student_utils
import validation  


students = [
    {
        "name": "Rahul",
        "age": 18,
        "cgpa": 8.2,
        "skills": ["Python", "SQL"]
    },
    {
        "name": "Anita",
        "age": 19,
        "cgpa": 9.1,
        "skills": ["Python", "Java"]
    }
]



print("=====STUDENT MANAGEMENT SYSTEM=====")
print("\n1. Display students")
print("2. Top student")
print("3. Find student")
print("4. Find student by skill")
print("5. Average CGPA")
print("6. Add student")
print("7. Remove student")
print("8. EXIT")


while True:
    choice = input("\nEnter your choice: ")

    if choice == "1":
        print(student_utils.display_students(students))
    elif choice == "2":
        print(student_utils.find_top_student(students))
    elif choice == "3":
        print(student_utils.find_student(students))
    elif choice == "4":
        print(student_utils.find_by_skill(students))
    elif choice == "5":
        print(student_utils.calculate_average_cgpa(students))
    elif choice == "6":
        print(student_utils.add_student(students))
    elif choice == "7":
        print(student_utils.remove_student(students))
    elif choice == "8":
        print("Exited")
        break
    else:
        print("Invalid choice. Please try again.")