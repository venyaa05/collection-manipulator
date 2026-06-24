students = []

print("---WELCOME TO THE STUDENT DATA ORGANIZER---")

while True:
    print("\nSelect an option")
    print("1.Add Student ")
    print("2.Display All Students")
    print("3.Update Student Information")
    print("4.Delete Student")
    print("5.Display Subjects Offered")
    print("6.Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("\nEnter Student Details:")
            student_id = int(input("Enter student ID:"))
            name = str(input("Enter your name:"))
            age = int(input("Enter your age:"))
            grade = str(input("Enter your grade(A-E):"))
            dob = input("Enter your birthdate(dd-mm-yyyy):")
            subjects_input = input("Enter subjects: ")
            student = {
                "student_id": student_id,
                "name": name,
                "age": age,
                "grade": grade,
                "dob": dob,
                "subjects": subjects
                }
            students.append(student)
            print("Student added successfully!")

        case 2:
            if len(students)==0:
                print("No student record found.")
            else:
                print("\n---Display All Students---")
                for student in students:
                    print("Student ID:",student["student_id"])
                    print("Name:",student["name"])
                    print("Age:",student["age"])
                    print("Grade:",student["grade"])
                    print("Date of Birth:",student["dob"])
                    print("Subjects:",student["subjects"])
                    print("------------------------------")

        case 3:
            update_id = int(input("Enter Student ID to update:"))
            found = False

            for student in students:
                if student["student_id"] == update_id:
                    found = True

                    print("\nWhat do you want to update?")
                    print("1.Student ID")
                    print("2.Name")
                    print("3.Age")
                    print("4.Grade")
                    print("5.DOB")
                    print("6.Subjects")

                    update_choice = int(input("Enter your choice:"))

                    match update_choice:
                        case 1:
                            student["student_id"] = int(input("Enter new Student ID:"))
                            print("Student ID updated successfully")

                        case 2:
                            student["name"] = input("Enter new name:")
                            print("Student name updated successfully")

                        case 3:
                            student["age"] = int(input("Enter new age:"))
                            print("Student age updated successfully")

                        case 4:
                            student["grade"] = input("Enter new grade:")
                            print("Student grade updated successfully")

                        case 5:
                            student["dob"] = input("Enter new Date Of Birth:")
                            print("Student Date Of Birth updated successfully")

                        case 6:
                            student["subjects"] = input("Enter new Subjects:")
                            print("Student Subject updated successfully")

                        case _:
                            print("Invalid choice")

                    break
                
            if found == False:
                print("Student ID not found")

        case 4:
            delete_id = int(input("Enter Student ID to delete:"))
            found = False

            for i in range(len(students)):
                if students[i]["student_id"] == delete_id:
                        del students[i] 
                        found = True
                        print("Student deleted successfully!")
                        break

            if found == False:
                 print("Student ID not found.")
                    
        case 5:
            all_subjects = set()

            for student in students:
                  all_subjects.add(student["subjects"])

            if len(all_subjects) == 0:
                print("No subjects found.")
            else:
                print("\nSubjects Offered:")
                for subject in all_subjects:
                      print(subject)

        case 6:
            print("Thank you for using Student Data Organizer!")
            break

        case _:
            print("Invalid choice! Please try again.")

                    



















                    
                                
















                            

            


























            

