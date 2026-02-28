class Account:
    """
    Represents a bank account with an ID, customer name, and balance.

    Attributes:
        id (str): The unique identifier for the account.
        customer (str): The name of the account holder.
        balance (float): The current balance of the account.
    """

    def __init__(self, id: str, customer: str, balance: float):
        """
        Initializes an Account instance.

        Args:
            id (str): The unique identifier for the account.
            customer (str): The name of the account holder.
            balance (float): The initial balance of the account.

        Raises:
            ValueError: If balance is negative.
        """
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.id = id
        self.customer = customer
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Deposits money into the account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Withdraws money from the account.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If amount is not positive or exceeds balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for withdrawal.")
        self.balance -= amount

    def get_balance(self) -> float:
        """
        Returns the current balance of the account.

        Returns:
            float: The current account balance.
        """
        return self.balance