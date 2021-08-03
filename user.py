# For this assignment, we'll add some functionality to the User class:

# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

    def display_user_balance(self):
        print(f'User: {self.name}, Balance: {self.account_balance}')

jonny = User("Jonny be Good", "jonny@codingdojo.com")
python = User("Python Monster", "python@codingdojo.com")
boaty = User("Boaty McBoatface", "boaty@codingdojo.com")

jonny.make_deposit(100)
jonny.make_deposit(500)
jonny.make_deposit(3000)
jonny.make_withdrawal(200)
jonny.display_user_balance()

python.make_deposit(100)
python.make_deposit(800)
python.make_withdrawal(100)
python.make_withdrawal(50)
python.display_user_balance()

boaty.make_deposit(2000)
boaty.make_withdrawal(100)
boaty.make_withdrawal(300)
boaty.make_withdrawal(10)
boaty.display_user_balance()

jonny.transfer_money(boaty,200)
jonny.display_user_balance()
boaty.display_user_balance()
