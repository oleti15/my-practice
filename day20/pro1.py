
def Mail(self):
    if '@' in email and'.' in email:
        print("valid")
    else:
        print("not valid")
email=input()
email[1:len(email)-1]
print(Mail(email))


