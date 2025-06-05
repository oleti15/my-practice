import conta as df
contacts={}
print("\n<===Contacts App===> ")
while True:
    try:
        print("\nChoices :")
        print("1.Add contact")
        print("2.View all contacts")
        print("3.Delete contact")
        print("4.Find contact")
        print("5.Edit contact")
        print("6.Exit")
        choice=int(input("Enter choice : "))
        if choice==1:
            df.add_contact(contacts)
        elif choice==2:
            df.view_contacts(contacts)
        elif choice==3:
            df.delete_contact(contacts)
        elif choice==4:
            df.find_contact(contacts)
        elif choice==5:
            df.edit_contact(contacts)
        else:
            print("Ok bye thank you!!!")
            break
    except ValueError:
        print(f"the error is ")
    else:
        print("there is no error occured")
    finally:
        print("the program end")
        

