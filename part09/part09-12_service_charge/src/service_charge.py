# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self, name: str, account: str, balance: float):
        self.__name = name
        self.__account = account
        self.__balance = balance

    def deposit(self, amount: float):
        self.balance += amount
        self.__service_charge()

    def withdraw(self, amount: float):
        self.balance -= amount
        self.__service_charge()

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def __service_charge(self):
        self.balance = self.balance * 0.99
