"""
Mini demo bank
"""

class Bank():

    def __init__(self):
        self.__pin = 123
        self.__balance= 10000

    def deposit(self):
        try:
            amount = float(input("Enter the amount to deposit: "))
        except ValueError:
            print("Amount must be a number")
            return
        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        self.__balance += amount
        print(f"Successfully deposited: {amount: 2f}")


    def withdraw(self):
        try:
            amount = float(input("Enter the amount to withdraw: "))
        except ValueError:
            print("Please enter a valid number.")
            return

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        if amount > self.__balance:
            print("Insufficient __balance.")
            return

        self.__balance -= amount
        print(f"Successfully withdrew: ₹{amount:.2f}")

    def __balance_check(self):
        print(f"__balance : {self.__balance}")

    def pin_check(self):

        times = 3

        while times > 0:
            try:
                pin_enter = int(input("Enter the __pin: "))
            except ValueError:
                print("__pin contains a number.")
                times-=1
                continue
            

            if pin_enter == self.__pin:
                print("Welcome.")
                return True

            times -= 1
            print(f"Incorrect __pin. Attempts remaining: {times}")

        print("Too many failed attemps.")
        return False


class Main(Bank):


    def run(self):
        while True:
            options = [
                "check __balance",
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

        
            if choice < 1 or choice > len(options):
                print("Invalid Choice.")
                continue

            if choice == 4:
                print("Exiting..")
                return

            if self.__pin_check():
                match choice:
                    case 1:
                        self.__balance_check()

                    case 2:
                        self.withdraw()

                    case 3:
                        self.deposit()

if __name__ =="__main__":
    bank = Main()
    bank.run()
        