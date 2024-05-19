import os

class ATM:
    def __init__(self, balance=0, pin=0000):
        # Constructor to initialize the ATM object with balance and PIN
        self.balance = balance  # Initialize the balance
        self.pin = pin  # Initialize the PIN

    def check_balance(self):
        # Method to check the balance
        return f"Current balance: Rs.{self.balance}"

    def withdraw(self, amount):
        # Method to withdraw money from the ATM
        if amount > self.balance:
            return "Insufficient funds."  # Return error message if balance is insufficient
        elif amount > 25000:
            return "Withdrawal amount exceeds the limit of Rs.25,000."  # Limit withdrawal amount
        else:
            self.balance -= amount  # Deduct the withdrawal amount from the balance
            self.update_balance_file()  # Update balance in the file
            return f"Withdrawal successful. Current balance: Rs.{self.balance}"  # Return success message

    def deposit(self, amount):
        # Method to deposit money into the ATM
        if amount > 50000:
            return "Deposit amount exceeds the limit of Rs.50,000."  # Limit deposit amount
        else:
            self.balance += amount  # Add the deposited amount to the balance
            self.update_balance_file()  # Update balance in the file
            return f"Deposit successful. Current balance: Rs.{self.balance}"  # Return success message

    def change_pin(self, new_pin):
        # Method to change the PIN
        self.pin = new_pin  # Change the PIN
        self.update_pin_file(new_pin)  # Update PIN in the file
        return "PIN changed successfully."  # Return success message

    def update_balance_file(self):
        # Method to update balance in the file
        try:
            file = open("balance.txt", "w")  # Open file in write mode
            file.write(str(self.balance))  # Write balance to the file
            file.close()  # Close the file after writing
        except FileNotFoundError:
            pass  # If file does not exist, do nothing

    def update_pin_file(self, new_pin):
        # Method to update PIN in the file
        try:
            file = open("pin.txt", "w")  # Open file in write mode
            file.write(str(new_pin))  # Write new PIN to the file
            file.close()  # Close the file after writing
        except FileNotFoundError:
            pass  # If file does not exist, do nothing

    @staticmethod
    def get_balance_from_file():
        # Static method to get balance from the file
        try:
            file = open("balance.txt", "r")  # Open file in read mode
            balance = file.read()  # Read balance from the file
            file.close()  # Close the file after reading
            return int(balance)  # Return the balance as an integer
        except FileNotFoundError:
            return 0  # If file does not exist, return 0 balance

    @staticmethod
    def get_pin_from_file():
        # Static method to get PIN from the file
        try:
            file = open("pin.txt", "r")  # Open file in read mode
            pin = file.read()  # Read PIN from the file
            file.close()  # Close the file after reading
            return int(pin)  # Return the PIN as an integer
        except FileNotFoundError:
            return 0000  # If file does not exist, return default PIN


# Initialize ATM object with initial balance and PIN
initial_balance = ATM.get_balance_from_file()
initial_pin = ATM.get_pin_from_file()
atm = ATM(initial_balance, initial_pin)

while True:
    print("--------------------------------------------------")
    print("          Welcome to the ATM machine. ")
    print("--------------------------------------------------")
    print()
    pin = int(input("Please enter your PIN: "))

    if pin != atm.pin:
        # Check if entered PIN is correct
        print("Incorrect PIN. Please try again.")
        continue

    os.system('cls')  # Clear screen for better display

    print("""       Menu                          
    -----------------------------
    1. Check Balance
    2. Withdraw
    3. Deposit
    4. Change PIN
    5. Exit""")

    option = int(input("\nEnter your choice: "))

    if option == 1:
        # Check balance option
        print("Current balance:", atm.check_balance())
        print()
    elif option == 2:
        # Withdraw option
        amount = float(input("Enter the amount to withdraw: "))
        print(atm.withdraw(amount))
        print()
    elif option == 3:
        # Deposit option
        amount = float(input("Enter the amount to deposit: "))
        print(atm.deposit(amount))
        print()
    elif option == 4:
        # Change PIN option
        new_pin = int(input("Enter your new PIN: "))
        print(atm.change_pin(new_pin))
        print()
    elif option == 5:
        # Exit option
        print("Thank you for using our ATM machine.")
        break
