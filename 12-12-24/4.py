print("Welcome to ABC Bank")

class Bank:
    acbal = 10000

    def deposit(self):
        dep = int(input("Enter the deposit amount: "))

        if dep < 100:
            print("Deposit amount should be greater than 100.")
        elif dep % 100 != 0:
            print("Deposit amount should be in multiples of 100.")
        elif dep > 50000:
            print("Deposit amount should be less than or equal to 50000.")
        else:
            Bank.acbal += dep  # Update balance
            print(f"Transaction successful. New balance: {Bank.acbal}")

    def withdrawn(self):
        for attempt in range(3):
            withdr = int(input("Enter the amount for withdrawal: "))

            if withdr < 100:
                print("Withdrawal amount should be greater than 100.")
            elif withdr % 100 != 0:
                print("Withdrawal amount should be in multiples of 100.")
            elif withdr > Bank.acbal:
                print("Insufficient funds.")
            elif withdr > 20000:
                print("You cannot withdraw more than 20000.")
            else:
                Bank.acbal -= withdr
                print(f"Withdrawal successful. Remaining balance: {Bank.acbal}")
                break
        else:
            print("Limit exceeded. Too many invalid attempts.")

    def viewOptions(self):
        print("1. Deposit\n"
              "2. Withdraw\n"
              "3. Balance Enquiry\n"
              "0. Exit\n")

    def balance_enquiry(self):
        print(f"Your current balance is: {Bank.acbal}")

    def validation(self):
        attempts = 0
        correct_pin = 1234
        while attempts < 3:
            pin = int(input("Enter PIN number: "))
            if pin == correct_pin:
                print("PIN validated successfully.")
                self.viewOptions()
                return True
            else:
                print("Invalid PIN. Please try again.")
                attempts += 1
        print("Account is locked due to too many incorrect attempts.")
        return False

obj = Bank()
if obj.validation():
    while True:
        option = int(input("Choose an option: "))

        if option == 1:
            obj.deposit()
        elif option == 2:
            obj.withdrawn()
        elif option == 3:
            obj.balance_enquiry()
        elif option == 0:
            print("Thank you for using ABC Bank!")
            break
        else:
            print("Invalid option. Please try again.")
