from abc import ABC, abstractmethod

# =========================
# ABSTRACTION
# =========================
class BankAccount(ABC):

    @abstractmethod
    def calculate_interest(self):
        pass


# =========================
# ENCAPSULATION
# =========================
class Account(BankAccount):
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # private variable

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")


# =========================
# INHERITANCE + POLYMORPHISM
# =========================
class SavingAccount(Account):
    def calculate_interest(self):
        return self.get_balance() * 0.04   # 4% interest


class CurrentAccount(Account):
    def calculate_interest(self):
        return self.get_balance() * 0.02   # 2% interest


# =========================
# MAIN PROGRAM
# =========================
sa = SavingAccount("Alice", 10000)
ca = CurrentAccount("Bob", 20000)

sa.deposit(2000)
ca.withdraw(5000)

print("Saving Account Balance:", sa.get_balance())
print("Saving Account Interest:", sa.calculate_interest())

print("Current Account Balance:", ca.get_balance())
print("Current Account Interest:", ca.calculate_interest())
