def add_student(gradebook):
    name=input("enetr student name:")
    marks=int(input("enter marks:"))
    mark_list=list(map(int,marks.split()))
    gradebook[name]=mark_list
    print(f"{name} The name is Added.")
def view_students(gradebook):
    if student not gradebook:
        print("No student found in gradebok") 
        return 
        print("\n All students")   
        for name,marks in gradebook.items():
            avg=sum(marks)/len(marks)
            print(f"found:{name}-marks:{marks}|avg:{avg:2f}")
            found=True
            if not found:
                print("student not found")
def update_student(gradebok):
    name=input("enter studentname to update marks:")
    if name in gradebook:
        marks=int(input("enter new markes:"))
        mark_list=list(map(int,marks.split()))
        gradebook[name]=mark_list
        print(f"{name}'s marks updated.")
    else:
        print("student not found")
def remove_student(gradebook):
    name=input("enter student name to remove:")
    if name in gradebook:
        del gradebook[name]
        print(f"{name} removed from gradebook")
    else:
        print("student not found")
