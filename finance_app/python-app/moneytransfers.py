from accounts import Account

class MoneyTransfer:
    @staticmethod
    def transfer_money(sender, receiver, amount):
        sender.withdraw(amount)
        receiver.deposit(amount)
