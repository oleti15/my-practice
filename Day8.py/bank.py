from abc import ABC , abstractmethod
class Account(ABC):
    @abstractmethod
    def get_balance(self):
        pass
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withDraw(self):
        pass
class SavingAccount(Account):
    __balance = 0
    def get_balance(self):
        # print("Balance = ",self.__balance)
        return self.__balance
    def deposit(self,amount):
        self.__balance+=amount
        print("Amount depoisted:",amount)
    def withDraw(self,amount):
        if self.__balance<amount:
            print("Not Enough Balance")
            return
        self.__balance-=amount
        print("Amount withdrawn:",amount)
class CurrentAccount(Account):
    __balance=0
    withDraw_limit=0
    def __init__(self,limit):
        self.withDraw_limit=limit
    def get_balance(self):
        # print("Balance = ",self.__balance)
        return self.__balance
    def deposit(self,amount):
        self.__balance+=amount
        print("Amount depoisted:",amount)
    def withDraw(self,amount):
        if self.__balance + self.withDraw_limit<amount:
            print("Not Enought Balance")
            return
        self.__balance-=amount
        print("Amount withdrawn:",amount)
class Bank:
    owner="bank"
    account_number=0
    def __init__(self,name,number,account_type="Saving"):
        self.owner=name
        self.account_number=number
        if account_type=="Saving":
            self.account=SavingAccount()
        if account_type=="Current":
            self.account=CurrentAccount(5000)
class Manager:
    def get_customer_info(self,bankAccount:Bank):
        print(f"Name:{bankAccount.owner}")
        print(f"AccountNumber:{bankAccount.account_number}")
        print("Account Type:",end="")
        if(type(bankAccount.account)==SavingAccount):
            print("Savings Account")
        else:
            print("Current Account")
        print(f"Balance:{bankAccount.account.get_balance()}")
    def __str__(self):
        return "Manager Object bro"
baby=Bank("Baby",1,"Saving")
baby.account.deposit(33)
print("<===== Jaya Account =====>")
jaya=Bank("Jaya",2,"Current")
jaya.account.deposit(34)
mn=Manager()
print("<===== Baby Account =====>")
mn.get_customer_info(baby)
print("<===== Sam Account =====>")
mn.get_customer_info(jaya)
print(type(mn) == Manager)