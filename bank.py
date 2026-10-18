"""
Mini demo bank
"""

class Bank():

    def __init__(self):
        self.pin = 123
        self.balance = 10000

    def deposit(self):
        amount = float(input("Enter the amount to deposit: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        self.balance += amount
        print(f"Successfully deposited: {amount: 2f}")


    def withdraw(self):
        amount = float(input("Enter the amount to wothdraw: "))
        self.balance -= amount

        if amount <= 0:
            print("Amount must be greater than 0.m")

        if amount > self.balance:
            print("Insufficient balance")
            return 

    def balance_check(self):
        print(f"Balance : {self.balance}")

    def pin_check(self):
        try:
            pin_enter = int(input("Enter the pin: "))
        except ValueError:
            print("PIN contains a number.")

        if pin_enter == self.pin:
            return True
        else:
            print("PIN incorrect")
            return False


class Main(Bank):


    def run(self):
        while True:
            options = [
                "check balance",
                "withdraw money",
                "deposit money",
                "exit"
            ]

            for i, option in enumerate(options, start=1):
                print(f"{i}: {option}")


            try:
                choice = int(input("Enter a valid choice: "))
            except ValueError:
                print("Please enter a valid input")
                continue

        
            if choice <= 0 or choice > len(option):
                print("Invalid Choice.")
                continue

            if self.pin_check():
                match choice:
                    case 1:
                        self.balance_check()

                    case 2:
                        self.withdraw()

                    case 3:
                        self.deposit()

                    case 4:
                        print("Exiting...")
                        return
                
if __name__ =="__main__":
    bank = Main()
    bank.run()
        