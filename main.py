from bank import Bank


def main():
    bank = Bank("My Bank", "123 Main St")
    while(True):
        print("-----Welcome to My Bank-----")
        print("1 - User")
        print("2 - Admin")
        option = input("Enter option: ")
        if option == "1":
            print("1 - Create Account")
            print("2 - Login")
            option = input("Enter option: ")
            if option == "1":
                name = input("Enter name: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                print("-----Account Type-----")
                print("1 - Savings")
                print("2 - Current")
                type = input("Enter option: ")
                if type == "1":
                    type = "Savings"
                elif type == "2":
                    type = "Current"
                bank.addAccount(name, email, address, type)
                print("Try logging in now with your account number")
            elif option == "2":
                account_number = input("Enter account number: ")
                for account in bank.accounts:
                    if account.account_number == account_number:
                        print("Login successful")
                        while(True):
                            print("-----Welcome to My Bank-----")
                            print("1 - Deposit")
                            print("2 - Withdraw")
                            print("3 - Transfer")
                            print("4 - Get Balance")
                            print("5 - Take Loan")
                            print("6 - History")
                            print("7 - Logout")
                            print("----------------------------")
                            option = input("Enter option: ")
                            if option == "1":
                                amount = int(input("Enter amount to deposit: "))
                                account.deposit(amount, bank)
                            elif option == "2":
                                amount = int(input("Enter amount to withdraw: "))
                                account.withdraw(amount, bank)
                            elif option == "3":
                                amount = int(input("Enter amount to transfer: "))
                                recipient_account_number = input("Enter recipient account number: ")
                                for recipient in bank.accounts:
                                    if recipient.account_number == recipient_account_number:
                                        account.transfer(amount, recipient)
                                        break
                                else:
                                    print("Recipient not found")
                            elif option == "4":
                                print("Your Current Balance is: ", account.getBalance())
                            elif option == "5":
                                amount = int(input("Enter amount to take loan: "))
                                account.take_loan(amount, bank)
                            elif option == "6":
                                account.get_history()
                            elif option == "7":
                                break
                        break
                else:
                    print("Account not found")
        elif option == "2":
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
                        print("-----Account Type-----")
                        print("1 - Savings")
                        print("2 - Current")
                        typeOption = input("Enter option: ")
                        type = None
                        if typeOption == "1":
                            type = "Savings"
                        elif typeOption == "2":
                            type = "Current"
                        bank.addAccount(name, email, address, type)
                    elif option == "2":
                        account_number = input("Enter account number: ")
                        bank.removeAccount(account_number)
                    elif option == "3":
                        bank.allUserAccounts()
                    elif option == "4":
                        bank.bankBalance()
                    elif option == "5":
                        bank.bankLoan()
                    elif option == "6":
                        print(f'Loan feature is currently {bank.loan_feature and "On" or "Off"}')
                        print("1 - On")
                        print("2 - Off")
                        option = input("Enter option: ")
                        if option == "1":
                            bank.onOrOffLoanFeature(True)
                        elif option == "2":
                            bank.onOrOffLoanFeature(False)
                        else:
                            print("Invalid option")
                    elif option == "7":
                        break
            else:
                print("Incorrect password")
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()