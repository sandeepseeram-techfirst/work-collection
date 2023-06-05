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

    stock1 = Stock("AAPL", 150)
    stock2 = Stock("GOOGL", 1000)
    print(stock1)
    print(stock2)

    for i in range(10):
        stock1.generate_price()
        stock2.generate_price()

    print(stock1)
    print(stock2)

if __name__ == "__main__":
    main()
