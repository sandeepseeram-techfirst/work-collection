from accounts import Account

class MoneyTransfer:
    @staticmethod
    def transfer_money(sender, receiver, amount):
        sender.withdraw(amount)
        receiver.deposit(amount)
    
    def __str__(self):
        return f"transfer_money {self.trans_id} with amount {transaction.amount}"