class Account:
    # static attribute
    minbal = 10000

    def __init__(self, acno: int, customer: str, balance: float):
        # Object Attributes
        self.acno = acno
        self.cutsomer = customer
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if self.balance - Account.minbal >= amount:
            self.balance -= amount
        else:
            print('Insufficient Balance!')

    def getbalance(self):
        return self.balance

    @staticmethod
    def getminbal():
        return Account.minbal


print('Minimum Balance : ', Account.getminbal())
a = Account(1, "Terry", 50000)
a.deposit(5000)
a.withdraw(20000)

print(a.getbalance())
