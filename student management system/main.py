import json
import os

DATA_FILE = "students.json"

# ----------------------------
# Student Class (OOP)
# ----------------------------
class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }


# ----------------------------
# File Handling Functions
# ----------------------------
def load_students():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_students(students):
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)


# ----------------------------
# System Features
# ----------------------------
def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    grade = input("Enter Grade: ")
    

    student = Student(student_id, name, age, grade)
    students = load_students()
    students.append(student.to_dict())
    save_students(students)

    print("✔ Student Added Successfully!")

def view_students():
    students = load_students()
    if not students:
        print("No students found.")
        return

    print("\n--- Student List ---")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Grade: {s['grade']}")

def search_student():
    student_id = input("Enter Student ID to search: ")
    students = load_students()

    for s in students:
        if s["id"] == student_id:
            print("\n--- Student Found ---")
            print(f"ID: {s['id']}")
            print(f"Name: {s['name']}")
            print(f"Age: {s['age']}")
            print(f"Grade: {s['grade']}")
            return

    print("❌ Student not found.")

def delete_student():
    student_id = input("Enter Student ID to delete: ")
    students = load_students()

    updated = [s for s in students if s["id"] != student_id]

    if len(updated) == len(students):
        print("❌ Student not found.")
    else:
        save_students(updated)
        print("🗑 Student deleted successfully!")


# ----------------------------
# Menu Loop
# ----------------------------
def menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

menu()
