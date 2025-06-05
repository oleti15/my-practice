import def_gradb 
gradebook={}
while True:
    print("\n Student Gradebook")
    print("1.Add Student")
    print("2.View All students")
    print("3.Search Student")
    print("4.Update Student")
    print("5.Remove Student")
    print("6.Exit")
    choice=input("Enter choice:")
    if choice=='1':
        def_gradb.add_student(gradebook)
    elif choice=='2':
        def_gradb.view_students(gradebook)
    elif choice=='3':
        def_gradb.search_student(gradebook)
    elif choice=='4':
        def_gradb.update_student(gradebook)
    elif choice=='5':
        def_gradb.remove_student(gradebook)
    elif choice=='6':
        print("Exit")
        break
    else:
        print(" Enter valid option:")
    
