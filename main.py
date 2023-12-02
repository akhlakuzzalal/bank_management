from bank import Bank
from person import Person


def main():
    bank = Bank("My Bank", "123 Main St")
    while(True):
        user = input("Are you a new user? (y/n): ")
        if user == "y":
            print("1 - Create Account")
            print("2 - Login")
            option = input("Enter option: ")
            if option == "1":
                name = input("Enter name: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                type = input("Enter type: ")
                bank.addAccount(name, email, address, type)
            elif option == "2":
                account_number = input("Enter account number: ")
                for account in bank.accounts:
                    if account.account_number == account_number:
                        print("Login successful")
                        while(True):
                            print("1 - Deposit")
                            print("2 - Withdraw")
                            print("3 - Transfer")
                            print("4 - Get Balance")
                            print("5 - Take Loan")
                            print("6 - History")
                            print("7 - Logout")
                            option = input("Enter option: ")
                            if option == "1":
                                amount = int(input("Enter amount: "))
                                account.deposit(amount)
                            elif option == "2":
                                amount = int(input("Enter amount: "))
                                account.withdraw(amount)
                            elif option == "3":
                                amount = int(input("Enter amount: "))
                                recipient_account_number = input("Enter recipient account number: ")
                                for recipient in bank.accounts:
                                    if recipient.account_number == recipient_account_number:
                                        account.transfer(amount, recipient)
                                        break
                                else:
                                    print("Recipient not found")
                            elif option == "4":
                                print("Balance: ", account.getBalance())
                            elif option == "5":
                                amount = int(input("Enter amount: "))
                                account.take_loan(amount)
                            elif option == "6":
                                account.get_history()
                            elif option == "7":
                                break
                        break
                else:
                    print("Account not found")
        elif user == "n":
            admin = input("Are you an admin? (y/n): ")
            if admin == "y":
                user_name = input("Enter username: ")
                password = input("Enter password: ")
                if user_name == "admin" and password == "123":
                    while(True):
                        print("1 - Add Account")
                        print("2 - Remove Account")
                        print("3 - Get All Accounts")
                        print("4 - Get Bank Balance")
                        print("5 - Get Bank Loan")
                        print("6 - On/Off Loan Feature")
                        print("7 - Logout")
                        option = input("Enter option: ")
                        if option == "1":
                            name = input("Enter name: ")
                            email = input("Enter email: ")
                            address = input("Enter address: ")
                            type = input("Enter type: ")
                            bank.addAccount(name, email, address, type)
                        elif option == "2":
                            account_number = input("Enter account number: ")
                            bank.removeAccount(account_number)
                        elif option == "3":
                            bank.getAllAccounts()
                        elif option == "4":
                            bank.bankBalance()
                        elif option == "5":
                            bank.bankLoan()
                        elif option == "6":
                            boolean = input("On or Off? (True/False): ")
                            bank.onOrOffLoanFeature(boolean)
                        elif option == "7":
                            break
                else:
                    print("Incorrect password")
            elif admin == "n":
                print("1 - Get All Accounts")
                print("2 - Get Bank Balance")
                print("3 - Get Bank Loan")
                print("4 - Logout")
                option = input("Enter option: ")
                if option == "1":
                    bank.getAllAccounts()
                elif option == "2":
                    bank.bankBalance()
                elif option == "3":
                    bank.bankLoan()
                elif option == "4":
                    break

if __name__ == "__main__":
    main()