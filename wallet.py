from transaction import Transaction
import transaction

class Wallet:
    def __init__(self):
        self.wallet_balance = 0.0
        self.transaction_history = []


    def deposit(self):
        self.wallet_balance = int(input("Enter the amount you want to deposit: "))
        if self.wallet_balance < 0:
            print("Invalid amount. Please enter a positive value.")
            self.deposit()
        else:
            transaction = Transaction("Deposit", self.wallet_balance)
            self.transaction_history.append(transaction)    
    def withdraw(self):
        amount = int(input("Enter the amount you want to withdraw: "))
        if amount <= self.wallet_balance and amount > 0:
            self.wallet_balance -= amount
            transaction = Transaction("Withdrawal", amount)
            self.transaction_history.append(transaction)
        else:
            print("Invalid amount or insufficient funds.")

    def get_balance(self):
        print("Your wallet balance is: " + str(self.wallet_balance))

    def show_history(self):
        print("Transaction history:")
        for transaction in self.transaction_history:
            print(transaction)

wallet = Wallet()
wallet.deposit()
wallet.withdraw()
wallet.get_balance()
wallet.show_history()
