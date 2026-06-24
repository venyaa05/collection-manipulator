<h1 align="center">📚 Collection Manipulator 📚</h1>
<h3 align="center">🎓 Interactive Student Record Management System using Python 🐍💻</h3>

<p align="center">
  <b>A beginner-friendly Python mini project to add, display, update, delete, and manage student records efficiently through a menu-driven console program ✨</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Project-Beginner%20Friendly-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Type-Console%20Application-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Completed-orange?style=for-the-badge" />
</p>

---

# 📖 Project Overview

**Collection Manipulator** is a simple and interactive Python project designed for **beginners** who want to practice Python fundamentals by building a mini **student record management system**.

This program allows the user to manage student records through a **menu-driven interface**.
The user can perform operations like:

* ➕ **Add student details**
* 📋 **Display all student records**
* ✏️ **Update student information**
* ❌ **Delete a student record**
* 📚 **Display all subjects offered**
* 🚪 **Exit the program**

This project is useful for understanding how Python handles **lists, dictionaries, sets, loops, conditional statements, and match-case** in a real mini-project.

---

# ✨ Features

✔️ Add student records with details like **ID, name, age, grade, DOB, and subjects**
✔️ Display all stored student records
✔️ Update student information using **Student ID**
✔️ Delete a student record from the list
✔️ Display all subjects entered in the system
✔️ Uses **list + dictionary + set** in one project
✔️ Menu-driven console application using **`match-case`**
✔️ Great beginner project for learning **CRUD operations in Python**

---

# 🛠️ Tech Stack

| Technology                   | Purpose                    |
| ---------------------------- | -------------------------- |
| **Python 3**                 | Programming Language       |
| **IDLE / VS Code / PyCharm** | To run the program         |
| **Console / CLI**            | User interaction interface |

---

# 📂 Project Structure

```bash id="owvm39"
Collection-Manipulator/
│── Collection Manipulator.py
│── README.md
│── data organiser 01.jpg
│── data organiser 02.jpg
│── data organiser 03.jpg
```

---

# 📸 Output Screenshots

<p align="center">
  <<img width="455" height="575" alt="data organiser 01" src="https://github.com/user-attachments/assets/0d0be88d-0354-4376-b77a-a4e49f085c75" />>
</p>

<p align="center">
  <<img width="437" height="668" alt="data organiser 02" src="https://github.com/user-attachments/assets/e0766e58-d541-4bda-9a1c-e6a6ae427563" />>
</p>

<p align="center">
  <<img width="459" height="627" alt="data organiser 03" src="https://github.com/user-attachments/assets/a07886be-d502-416d-91f2-dc07f5068783" />>
</p>

---

# 💻 Source Code

```python id="x7v8pa"
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
            subjects = input("Enter subjects: ")

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
            if len(students) == 0:
                print("No student record found.")
            else:
                print("\n---Display All Students---")
                for student in students:
                    print("Student ID:", student["student_id"])
                    print("Name:", student["name"])
                    print("Age:", student["age"])
                    print("Grade:", student["grade"])
                    print("Date of Birth:", student["dob"])
                    print("Subjects:", student["subjects"])
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
```

---

# ▶️ How to Run the Project

## Step 1: Save the Python file

Save your program with the file name:

```bash id="qdr32k"
Collection Manipulator.py
```

## Step 2: Open in Python IDE

You can run it in:

* **Python IDLE**
* **VS Code**
* **PyCharm**

## Step 3: Run the Program

Execute the file and choose an option from the menu.

## Step 4: Perform Student Operations

You can:

* add a student
* display all students
* update any student record
* delete a student
* display subjects offered
* exit the program

---

# 📚 Concepts Used

* `input()`
* `int()`, `str()`
* `list`
* `dictionary`
* `set`
* `for loop`
* `if-else`
* `match-case`
* CRUD operations
* menu-driven programming

---

# 🎯 Learning Objectives

By making this project, you can practice:

* storing multiple records in a **list**
* storing structured student data in a **dictionary**
* using **sets** for unique subject handling
* building a **menu-driven Python application**
* performing **CRUD operations**
* updating and deleting records dynamically
* using loops and conditions in real mini-projects

---

# 📝 Sample Output

```bash id="1pt9ru"
---WELCOME TO THE STUDENT DATA ORGANIZER---

Select an option
1.Add Student
2.Display All Students
3.Update Student Information
4.Delete Student
5.Display Subjects Offered
6.Exit

Enter your choice: 1

Enter Student Details:
Enter student ID: 101
Enter your name: Venya
Enter your age: 20
Enter your grade(A-E): A
Enter your birthdate(dd-mm-yyyy): 20-10-2005
Enter subjects: Python, DAA, DBMS

Student added successfully!
```

---

# 🧾 Example Student Record Format

```python id="we5s4d"
{
    "student_id": 101,
    "name": "Venya",
    "age": 20,
    "grade": "A",
    "dob": "20-10-2005",
    "subjects": "Python, DAA, DBMS"
}
```

---

# 🚀 Why this project is useful

This project is a great **foundation-building exercise** because it combines:

* user interaction
* structured data storage
* CRUD operations
* Python data structures
* menu-driven logic
* record management concepts

It is perfect for students who are learning Python and want to create a practical **Student Management mini project**.

---

# 🔮 Future Improvements

This project can be improved further by adding:

* 💾 **File handling** to save student data permanently
* 🗄️ **Database support** using MySQL or SQLite
* 🔍 **Search student by ID**
* 📊 **Student count and statistics**
* 🧹 **Input validation**
* 🖥️ **GUI version using Tkinter**
* 🌐 **Web version using Flask/Django**

---

</p>
