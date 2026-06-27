from bank_account import Bank_Account

account1 = Bank_Account("Arda", 1000)
account2 = Bank_Account("Ayse", 500)

account1.deposit(500)
account1.withdraw(200)
account1.transfer(account2, 300)

print(account1.show_transactions())
print(account2.show_transactions())