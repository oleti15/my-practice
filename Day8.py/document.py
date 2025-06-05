from abc import ABC, abstractmethod
class Account(ABC):
    @abstractmethod
    def get_balance(self):
        pass
    @abstractmethod
    def deposit(self, amount):
        pass
    @abstractmethod
    def withDraw(self, amount):
        pass
class SavingAccount(Account):
    def __init__(self):
        self.__balance = 0
    def get_balance(self):
        return self.__balance
    def deposit(self,amount):
        self.__balance+=amount
        print("Amount deposited:", amount)
    def withDraw(self,amount):
        if self.__balance<amount:
            print("Not Enough Balance")
            return
        self.__balance-=amount
        print("Amount withdrawn:",amount)
class CurrentAccount(Account):
    def __init__(self, limit):
        self.__balance=0
        self.withDraw_limit=limit
    def get_balance(self):
        return self.__balance
    def deposit(self, amount):
        self.__balance+=amount
        print("Amount deposited:", amount)
    def withDraw(self, amount):
        if self.__balance + self.withDraw_limit< amount:
            print("Not Enough Balance")
            return
        self.__balance -= amount
        print("Amount withdrawn:", amount)
from account import SavingAccount, CurrentAccount

class Bank:
    def __init__(self, name, number, account_type="Saving"):
        self.owner = name
        self.account_number = number
        if account_type == "Saving":
            self.account = SavingAccount()
        elif account_type == "Current":
            self.account = CurrentAccount(5000)
from account import SavingAccount

class Manager:
    def get_customer_info(self, bankAccount):
        print(f"Name: {bankAccount.owner}")
        print(f"Account Number: {bankAccount.account_number}")
        print("Account Type:", end=" ")
        if isinstance(bankAccount.account, SavingAccount):
            print("Savings Account")
        else:
            print("Current Account")
        print(f"Balance: {bankAccount.account.get_balance()}")

    def __str__(self):
        return "Manager Object bro"
from bank import Bank
from manager import Manager

print("<===== Creating Baby's Account =====>")
baby = Bank("Baby", 1, "Saving")
baby.account.deposit(33)

print("<===== Creating Jaya's Account =====>")
jaya = Bank("Jaya", 2, "Current")
jaya.account.deposit(34)

mn = Manager()

print("\n<===== Baby Account Info =====>")
mn.get_customer_info(baby)

print("\n<===== Jaya Account Info =====>")
mn.get_customer_info(jaya)

print("\nIs mn a Manager?", isinstance(mn, Manager))
