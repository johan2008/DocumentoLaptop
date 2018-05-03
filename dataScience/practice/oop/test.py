class BankAccount:
	def __init__(self):
		self.balance = 0

	def withdraw(self, amount):
		self.balance -= amount
		return self.balance

	def deposit(self,amount):
		self.balance += amount
		return self.balance


class MinimunBalanceAccount(BankAccount):
	def __init__(self, minimin_balance):
		BankAccount.__init__(self)
		self.minimun_balance = minimun_balance

	def withdraw(self, amount):
		if self.balance - amount < self.minimun_balance:
			print("Sorry, minimun balance must be maintained")
		else:
			BankAccount.withdraw(self, amount)

a = BankAccount()
b = BankAccount()

print(a.deposit(100))
print(b.deposit(50))
print(b.withdraw(10))
print(a.withdraw(10))
