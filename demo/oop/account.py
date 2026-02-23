class InsufficientBalanceError(Exception):
    def __init__(self, amount, balance):
        self.message = f"Cannot withdraw {amount} when balance is {balance}"

    def __str__(self):
        return self.message


class Account:
    # static attribute
    minbal = 10000

    def __init__(self, acno: int, customer: str, balance: float):
        # Object Attributes
        self.acno = acno
        self.cutsomer = customer
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError('Invalid Amount!')

        self.balance += amount

    def withdraw(self, amount: float):
        if self.balance - Account.minbal >= amount:
            self.balance -= amount
        else:
            raise InsufficientBalanceError(amount, self.balance)

    def getbalance(self):
        return self.balance

    @staticmethod
    def getminbal():
        return Account.minbal


print('Minimum Balance : ', Account.getminbal())
a = Account(1, "Terry", 50000)
try:
    a.deposit(5000)
    a.withdraw(200000)
except ValueError as ex:
    print(ex)

print(a.getbalance())
