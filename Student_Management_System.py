student_data = [
    {"ID":710033,"Name":"Nivetha","Course":"Artifical Intelligence"},
    {"ID":710010,"Name":"Gojo","Course":"Artifical Intelligence"},
    {"ID":710020,"Name":"Ash","Course":"Artifical Intelligence"},
    {"ID":710030,"Name":"kento","Course":"Artifical Intelligence"}
]
while True:
    choice = int(input("=== STUDENT MANAGEMENT SYSTEM ===\n1. Add Student\n2. View All Students\n3. Search Student by ID\n4. Exit\nEnter a choice:"))
    if choice == 1:
        Studend_ID = int(input("Enter Student ID:"))
        Student_Name = input("Enter a Student Name:")
        Student_course = input("Enter Course Name:")
        new_data = dict(ID = Studend_ID,Name = Student_Name,Course = Student_course)
        student_data.append(new_data)
        print(f"Student \"{Student_Name}\" is successfully Added to Student Database")
        print()
    elif choice == 2:
        if not student_data :
            print("Student DataBase is currently empty")
            print()
        else:
            print(f"--- All Students ---          Record:{len(student_data)}")
            print()
            for i in student_data:
                for j,k in i.items():
                    print(f"{j}:{k}",end=" | ")
                print("\n")
            print()
    elif choice == 3:
        Search_id = int(input("Enter Student ID:"))
        found = False
        for student in student_data:
            if student["ID"] == Search_id:
                print()
                print("-----Student Data Found------")
                print("Student ID:",student["ID"])
                print("Student Name:",student["Name"])
                print("Course Name:",student["Course"])
                print()
                found = True
                break
        if not found:
            print(f"Error: Student with ID {Search_id} not found.\n")

    elif choice == 4:
        print("Good Bye")
        break
    else:
        print("Invalid Choice")
        print("Please Try Again")

