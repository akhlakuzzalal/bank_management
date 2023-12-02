from nanoid import generate


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Name: " + self.name + " Age: " + str(self.age)
    

class User(Person):
    def __init__(self, name, email, address, type):
        super().__init__(name)
        self.email = email
        self.address = address
        self.type = type
        self.__balance = 0
        self.account_number = None
        self.history = []
        self.loanPending = 2

    def getBalance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount
        self.history.append({"type": "deposit", "amount": amount, "balance": self.__balance})

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            self.history.append({"type": "withdraw", "amount": amount, "balance": self.__balance})
        else:
            print("Withdrawal amount exceeded")

    def take_loan(self, amount):
        if self.loanPending > 0:
            self.__balance += amount
            self.history.append({"type": "loan", "amount": amount, "balance": self.__balance})
            self.loanPending -= 1
        else:
            print("You have reached your loan limit")

    
    def transfer(self, amount, recipient):
        if self.__balance >= amount:
            self.__balance -= amount
            recipient.__balance += amount
            self.history.append({"type": "transfer", "amount": amount, "balance": self.__balance})
            recipient.history.append({"type": "transfer", "amount": amount, "balance": recipient.__balance})
        else:
            print("Transfer amount exceeded")


    def __repr__(self):
        return super().__repr__() + " Username: " + self.email + " Address: " + self.address + " Type: " + self.type + " Balance: " + str(self.__balance) + " Account Number: " + str(self.account_number) + " Loan Pending: " + str(self.loanPending)
    