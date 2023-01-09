class Bank:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'{amount} deposited')
        self.display_balance()

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient balance')
        else:
            self.balance -= amount
            print(f'{amount} withdrawn')
        self.display_balance()

    def display_balance(self):
        print(f'Current balance: {self.balance}')

class BankAccount(Bank):
    def __init__(self, name, balance, account_type):
        Bank.__init__(self, name, balance)
        self.account_type = account_type

    def __str__(self):
        return f'Name: {self.name}\nAccount type: {self.account_type}\nBalance: {self.balance}'

class BankManager:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def remove_account(self, account):
        self.accounts.remove(account)

    def display_accounts(self):
        for account in self.accounts:
            print(account)

def main():
    manager = BankManager()

    while True:
        print('Enter 1 to create a new account')
        print('Enter 2 to delete an account')
        print('Enter 3 to display all accounts')
        print('Enter 4 to exit')
        choice = int(input('Enter choice: '))

        if choice == 1:
            name = input('Enter name: ')
            balance = float(input('Enter balance: '))
            account_type = input('Enter account type: ')
            manager.add_account(BankAccount(name, balance, account_type))
        elif choice == 2:
            name = input('Enter name: ')
            account = next(a for a in manager.accounts if a.name == name)
            manager.remove_account(account)
        elif choice == 3:
            manager.display_accounts()
        elif choice == 4:
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()
