class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

class StudentManager:
    def __init__(self):
        self.students = [
            Student("საბა ბერიძე", 101, "A"),
            Student("ალექსანდრე გორდელაძე", 102, "B"),
            Student("ლიზი სახოკია", 103, "C"),
            Student("ნათია ფრუიძე", 104, "A"),
            Student("გია დვალიშვილი", 105, "B"),
            Student("მონიკა ბუცხრიკიძე", 106, "C"),
            Student("დიმიტრი თუთბერიძე", 107, "A"),
            Student("ლაშა ბრეგაძე", 108, "B"),
        ]

    def add_student(self, student):
        self.students.append(student)

    def view_all_students(self):
        if not self.students:
            print("No students available.")
        else:
            print("List of Students:")
            for student in self.students:
                print(f"Name: {student.name}, Roll Number: {student.roll_number}, Grade: {student.grade}")

    def search_student_by_roll_number(self, roll_number):
        found_student = None
        for student in self.students:
            if student.roll_number == roll_number:
                found_student = student
                break
        return found_student

    def update_grade(self, roll_number, new_grade):
        student = self.search_student_by_roll_number(roll_number)
        if student:
            student.grade = new_grade
            print("Grade updated successfully.")
        else:
            print("Student not found.")

def main():
    student_manager = StudentManager()

    while True:
        print("\nStudent Management System")
        print("1) Add a new student")
        print("2) View all students")
        print("3) Search for a student by id number")
        print("4) Update student's grade")
        print("5) Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name of the student: ")
            roll_number = int(input("Enter the id number of the student: "))
            grade = input("Enter the grade of the student: ")
            student = Student(name, roll_number, grade)
            student_manager.add_student(student)
            print("Student added successfully.")
        elif choice == "2":
            student_manager.view_all_students()
        elif choice == "3":
            roll_number = int(input("Enter the roll number of the student to search: "))
            student = student_manager.search_student_by_roll_number(roll_number)
            if student:
                print(f"Name: {student.name}, Roll Number: {student.roll_number}, Grade: {student.grade}")
            else:
                print("Student not found.")
        elif choice == "4":
            roll_number = int(input("Enter the roll number of the student to update grade: "))
            new_grade = input("Enter the new grade: ")
            student_manager.update_grade(roll_number, new_grade)
        elif choice == "5":
            print("Thank you for using the Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
