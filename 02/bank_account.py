from datetime import datetime

class Bank_Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
        self.transactions = []

    def _write_log(self, message):
        with open("transaction.txt", "a", encoding="utf-8") as file:
            file.write(message + "\n")

    def _get_time(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def deposit(self, amount):
        if amount < 0:
            return "Invalid Amount"

        self.__balance += amount

        log = f"{self._get_time()} | Deposit: +{amount}"
        self.transactions.append(log)
        self._write_log(log)

        return "Deposit successful"

    def withdraw(self, amount):
        if amount < 0:
            return "Invalid Amount"

        if amount > self.__balance:
            return "Insufficient Balance"

        self.__balance -= amount

        log = f"{self._get_time()} | Withdraw: -{amount}"
        self.transactions.append(log)
        self._write_log(log)

        return "Withdraw successful"

    def transfer(self, target_account, amount):
        if amount < 0:
            return "Invalid Amount"

        if amount > self.__balance:
            return "Insufficient Balance"

        self.__balance -= amount
        target_account.deposit(amount)

        log1 = f"{self._get_time()} | Transfer to {target_account.owner}: -{amount}"
        log2 = f"{self._get_time()} | Transfer from {self.owner}: +{amount}"

        self.transactions.append(log1)
        target_account.transactions.append(log2)

        self._write_log(log1)
        self._write_log(log2)

        return "Transfer successful"

    def show_transactions(self):
        return self.transactions