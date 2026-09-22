students = [
    {"id": 1, "name": "Azan", "marks": 90},
    {"id": 2, "name": "Faizan", "marks": 90},
    {"id": 3, "name": "Mubeen", "marks": 90}
]

while True:

    print("\n=== STUDENT MANAGEMENT SYSTEM BY AZAN ===")
    print("1. Show Students")
    print("2. Search Student")
    print("3. Add Student")
    print("4. Exit")

    choice = input("Enter choice: ")
    if choice == "1":

        for student in students:
            print(
                "ID:", student["id"],
                "| Name:", student["name"],
                "| Marks:", student["marks"]
            )
    elif choice == "2":

        student_search = input("Enter student name to search: ")

        found = False

        for student in students:

            if student["name"].lower() == student_search.lower():

                print("Student found!")
                print("ID:", student["id"])
                print("Name:", student["name"])
                print("Marks:", student["marks"])

                found = True
                break

        if found == False:
            print("Student not found!")

    elif choice == "3":

        student_id = int(input("Enter student ID: "))
        student_name = input("Enter student name: ")
        student_marks = int(input("Enter student marks: "))

        new_student = {
            "id": student_id,
            "name": student_name,
            "marks": student_marks
        }
        students.append(new_student)

        print("Student added successfully!")
    elif choice == "4":

        print("Program closed.")
        break

    else:
        print("Invalid choice!")