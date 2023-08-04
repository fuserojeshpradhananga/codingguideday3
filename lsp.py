class Overdraft:
    def __init__(self, overdraft_limit):
        self.overdraft_limit = overdraft_limit

    def can_withdraw(self, balance, amount):
        return (balance + self.overdraft_limit) >= amount


class SavingsAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Insufficient funds!")


class CheckingAccount:
    def __init__(self, balance, overdraft_limit):
        self.balance = balance
        self.overdraft = Overdraft(overdraft_limit)

    def withdraw(self, amount):
        if self.overdraft.can_withdraw(self.balance, amount):
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Exceeds overdraft limit or insufficient funds!")


def perform_bank_actions(account):
    account.withdraw(100)
    account.withdraw(200)
    account.withdraw(500)


if __name__ == "__main__":
    # Creating instances of SavingsAccount and CheckingAccount
    savings_account = SavingsAccount(500)
    checking_account = CheckingAccount(1000, overdraft_limit=200)

    # Performing actions on both accounts
    print("Savings Account:")
    perform_bank_actions(savings_account)

    print("\nChecking Account:")
    perform_bank_actions(checking_account)
