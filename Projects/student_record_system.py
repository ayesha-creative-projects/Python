# Student Record System

students = []  # List to store all students

while True:
    print("\n----- STUDENT MENU -----")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Name")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        marks = input("Enter student marks: ")
        student = {"name": name, "age": age, "marks": marks}
        students.append(student)
        print(f"Student {name} added!")
        
    elif choice == "2":
        if students:
            print("\nAll Students:")
            for s in students:
                print(s)
        else:
            print("No students found.")
            
    elif choice == "3":
        search_name = input("Enter name to search: ")
        found = False
        for s in students:
            if s["name"].lower() == search_name.lower():
                print("Student Found:", s)
                found = True
        if not found:
            print("Student not found.")
            
    elif choice == "4":
        print("Exiting student system. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
