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

    def deposit(self, account_number, amount):
        for account in self.accounts:
            if account.account_number == account_number:
                account.deposit(amount)
                self.__balance += amount
                print("Deposit successful")
                return
        print("Account not found")
        
    def withdraw(self, account_number, amount):
        for account in self.accounts:
            if account.account_number == account_number:
                account.withdraw(amount)
                self.__balance -= amount
                print("Withdrawal successful")
                return
        print("Account not found")

    def take_loan(self, account_number, amount):
        for account in self.accounts:
            if account.account_number == account_number:
                if self.loan_feature:
                    account.take_loan(amount)
                    self.__loan_ammount += amount
                    print("Loan taken")
                    return
                else:
                    print("Loan feature is off")
                    return
        print("Account not found")

    def transfer(self, sender_account_number, recipient_account_number, amount):
        for sender in self.accounts:
            if sender.account_number == sender_account_number:
                for recipient in self.accounts:
                    if recipient.account_number == recipient_account_number:
                        sender.transfer(amount, recipient)
                        print("Transfer successful")
                        return
                print("Recipient account not found")
                return
        print("Sender account not found")

    def __repr__ (self):
        print("Bank Name:", self.name)
        print("Bank Address:", self.address)