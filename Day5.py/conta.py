
def add_contact(contacts):
    try:
        name=input("Enter Contact Name:")
        mobile=int(input("Enter mobile number:"))
        contacts[name]=mobile
        file=open("baby.txt","a")
        file.write(f"{name}:{mobile}")
        print("add contact successfully.")
    except ValueError:
        print(" please enter valid mobile number")
def view_contacts(contacts):
    print("\n")
    try:
        file= open("baby.txt","r") 
        lines=file.readlines()
        for items in lines:
            if ':' in item:
                name,mobie=item.split(":")
                print(f"name:{name},mobile:{mobile}")
    except Exception as e:
        print("Error reading contacts from file:", e)
    for i in contacts:
        print(f"{i}:{contacts[i]}")
def delete_contact(contacts):
    try:
        name_to_delete=input("Enter contact name to delete:")
        if name_to_delete in contacts:
            del contacts[name_to_delete]
        file=open("baby.txt","w") 
        for name,mobile in contacts.items():
            file.write(f"{name}:{mobile}\n")
        print("deleted contact",name_to_delete)
    except Exception as e:
        print("Error deleting contact:", e)

def find_contact(contacts):
    query=input("Enter name to search:")
    found=False
    for key in contacts:
        if query in key:
            print(f"{key}=>{contacts[key]}")
            found=True
    if not found:
        print("Query not Found!!!")
def edit_contact(contacts):
    try:
        name_to_edit =input("Enter contact name to edit:")
        if name_to_edit in contacts:
            number=int(input("Enter new number:"))
            contacts[name_to_edit]=number
            file=open("baby.txt","w")
            for name,mobile in contactas.items():
                file.write(f"{name}:{mobile}\n")
            print("Edited contact:",name_to_edit)
        else:
            print("contact not found")
    except ValueError:
                print("invalid number")
    