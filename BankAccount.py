class BankAccount:
    """
    Represents a bank account
    using OOM paradigm in Python
    """
    def __init__(self, balance, account_num, name, ssn):
        if balance < 100:
            raise ValueError("Balance must be greater than $100")
        elif balance > 10000:
            raise ValueError("Balance must be less than $10,000")
        self.balance = balance
        self.account_num = account_num
        self.name = name
        self.ssn = ssn

    def __str__(self):
        return '${} | {} | {} | {}'.format(self.balance, self.account_num, self.name, self.ssn)

    def check_balance(self):
        """

        :return: customer balance
        """
        return self.balance

    def deposit(self,amount):
        """
        :param amount: amount to deposit
        :return: the new balance
        """

        if 1 < amount < 10000:
            self.balance += amount
        else:
            print("Invalid amount. Must be less than $1 and less than $10,000")

    def withdrawl(self,amount):
        """
        The withdrawl functionality
        of a bank account
        :param amount:  amount of a window
        :return: the balance
        """

        if amount < 1 or amount > self.balance:
            print("Invalid amount")
        self.balance -= amount

    def delete_account(self):
        """
        This method will remove this
        Customer's account or will remove this object from memory
        :return:
        """

        user_input = input("Do you really want to delete?  Type 'y' for yes or 'n' for no")
        if user_input == 'y':
            self.balance = 0
        elif uesr_input == 'n':
            print('Thanks for banking with us')
        else:
            print('Enter a valid input')

b1 = BankAccount(500, '3333', 'Mike', '3334444')
print(b1)
print(b1.balance)
b1.deposit(1000)
print(b1.balance)
b1.deposit(1500)
print(b1.balance)
b1.withdrawl(50)
print(b1.balance)
b1.deposit(5000)
print(b1.balance)
b1.delete_account()
print(b1.balance)