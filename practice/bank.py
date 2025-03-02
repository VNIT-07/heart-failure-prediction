print("--------- Welcome to the Bank System --------")
menu = """
1. Create an account
2. Deposit money
3. Withdraw money
4. Check account balance
5. Exit the system
"""
print(menu)

balance = 1.0
opening_depo = balance

def create_account():
    global name, password, balance
    name = input("Enter the Account Holder's Name: ")
    balance = float(input("Enter the Initial Balance for the Account: "))
    while True:
        password = input("Set a Password for the Account: ")
        confirm_password = input("Confirm the Password: ")
        if password == confirm_password:
            print("Account created successfully! You can now access your account.\n")
            break
        else:
            print("Passwords do not match. Please try again.\n")

def deposit_money():
    global balance, amount, opening_depo
    AccCreated = input("Is the account already created? (Y/N): ")
    if AccCreated.upper() == "N":
        print("-- Redirecting to Create Account Process --")
        return create_account()
    else:
        amount = int(input("Enter the Amount to Deposit: "))
        balance += amount
        print(f"Opening Deposit Amount: {opening_depo}")
        print(f"Deposited Amount: {amount}")
        print(f"Updated Account Balance: {balance}\n")

def withdraw_money():
    global balance, amount
    AccCreated = input("Is the account already created? (Y/N): ")
    if AccCreated.upper() == "N":
        print("-- Redirecting to Create Account Process --")
        return create_account()
    else:
        amount = float(input("Enter the Amount to Withdraw: "))
        if amount > balance:
            print(f"Insufficient balance! Your current balance is: {balance}")
        else:
            balance -= amount
            print(f"Amount of {amount} withdrawn successfully.")
            print(f"Updated Account Balance: {balance}\n")

def checkBalance():
    global balance
    AccCreated = input("Is the account already created? (Y/N): ")
    if AccCreated.upper() == "N":
        print("-- Redirecting to Create Account Process --")
        return create_account()
    else:
        print(f"Your Current Account Balance is: {balance}\n")

while True:
    opt = int(input("Choose an Option from the Menu: "))
    if opt == 1:
        create_account()
    elif opt == 2:
        deposit_money()
    elif opt == 3:
        withdraw_money()
    elif opt == 4:
        checkBalance()
    elif opt == 5:
        print("Exiting the system. Thank you for using our services!")
        exit()
    else:
        print("Invalid option. Please choose a valid option from the menu.")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
