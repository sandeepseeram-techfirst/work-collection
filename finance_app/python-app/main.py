from accounts import Account
from moneytransfers import MoneyTransfer
from stocks import Stock

def main():
    acc1 = Account("1", 10000, "John")
    acc2 = Account("2", 5000, "Jane")
    print(acc1)
    print(acc2)

    MoneyTransfer.transfer_money(acc1, acc2, 500)
    print(acc1)
    print(acc2)

 