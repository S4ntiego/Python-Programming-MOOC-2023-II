# Write your solution here:
class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, deposit: float):
        if deposit < 0:
            raise ValueError(
                "Invalid deposit amount. Amount must be greater than or equal to zero."
            )
        self.balance += deposit

    def eat_lunch(self):
        self.balance -= 2.6 if self.balance >= 2.6 else 0

    def eat_special(self):
        self.balance -= 4.6 if self.balance >= 4.6 else 0

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"


peters_card = LunchCard(20)
graces_card = LunchCard(30)
peters_card.eat_special()
graces_card.eat_lunch()
print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")
peters_card.deposit_money(20)
graces_card.eat_special()
print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")
peters_card.eat_lunch()
peters_card.eat_lunch()
graces_card.deposit_money(50)
print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")
