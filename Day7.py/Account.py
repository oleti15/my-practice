class Account:
    name=""
    balance=0
    def fun(self,name):
        print(f"the Account person is {name} ")
class Saving(Account):
    def deposit(self,balance):
        print(f"the deposited amount {balance}")
    def withdraw(self,balance):
        print(f"the with draw amount is {balance}")
x=Saving()
x.fun("baby")
x.withdraw(1000)
x.deposit(100)

