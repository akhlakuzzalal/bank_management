from nanoid import generate

from person import User


class Bank:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.accounts = []
        self.__balance = 0
        self.__loan_ammount = 0
        self.loan_feature = True

    def addAccount(self, name, email, address, type):
        account_number = generate('1234567890', 10)
        new_account = User(name, email, address, type)
        new_account.account_number = account_number
        self.accounts.append(new_account)
        print(f'Account created with account number: {account_number}')

    def removeAccount(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                print("Account removed")
                return
        print("Account not found")

    def allUserAccounts(self):
        print("------------All accounts------------")
        for account in self.accounts:
            print(f'Account Number: {account.account_number}\t Name: {account.name}\t Email: {account.email}\t Type: {account.type}')
        print("------------------------------------")

    def bankBalance(self):
        print("Total Balance: ", self.__balance)

    def bankLoan(self):
        print("Total Loan: ", self.__loan_ammount)

    def onOrOffLoanFeature(self, boolean):
        self.loan_feature = boolean

    def deposit(self, amount):
        self.__balance += amount
        return True
        
    def withdraw(self, amount):
        self.__balance -= amount
        return True

    def take_loan(self, amount):
        if self.loan_feature:
            self.__loan_ammount += amount
            return True
        else:
            print("Loan feature is currently off")
            return False

    def __repr__ (self):
        print("Bank Name:", self.name)
        print("Bank Address:", self.address)