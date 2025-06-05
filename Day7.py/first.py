def add_student(gradebook):
    name = input("Enter student name: ")
    marks = input("Enter marks separated by spaces: ")
    mark_list = list(map(int, marks.split()))
    gradebook[name] = mark_list
    print(f"{name} added successfully.")

def view_students(gradebook):
    if not gradebook:
        print("No students found.")
        return
    print("\n--- All Students ---")
    for name, marks in gradebook.items():
        avg = sum(marks) / len(marks)
        print(f"{name} - Marks: {marks} | Avg: {avg:.2f}")

def search_student(gradebook):
    search_name = input("Enter student name to search: ").lower()
    found = False
    for name, marks in gradebook.items():
        if search_name in name.lower():
            avg = sum(marks) / len(marks)
            print(f"Found: {name} - Marks: {marks} | Avg: {avg:.2f}")
            found = True
    if not found:
        print("Student not found.")

def update_student(gradebook):
    name = input("Enter student name to update marks: ")
    if name in gradebook:
        marks = input("Enter new marks separated by spaces: ")
        mark_list = list(map(int, marks.split()))
        gradebook[name] = mark_list
        print(f"{name}'s marks updated.")
    else:
        print("Student not found.")

def remove_student(gradebook):
    name = input("Enter student name to remove: ")
    if name in gradebook:
        del gradebook[name]
        print(f"{name} removed from gradebook.")
    else:
        print("Student not found.")