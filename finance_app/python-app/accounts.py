class Account:
    def __init__(self, acc_id, balance, owner):
        self.acc_id = acc_id
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        self.balance += amount



    def __str__(self):
        return f"Account {self.acc_id} owned by {self.owner} with balance {self.balance}"
