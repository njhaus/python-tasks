# TODO
from sys import exit


def main():
    while True:
        try:
            cash = float(input("Change owed: "))
        except ValueError:
            print("Please enter a number greate than 0")
        else:
            print(cash)
            if cash < 0.01:
                print("Please enter a number greater than 0")
            else:
                coins = 0
                quarter = float(0.25)
                dime = float(0.1)
                nickel = float(0.05)
                penny = float(0.01)
                coin_types = [quarter, dime, nickel, penny]
                current_coin = 0
                while cash > 0:
                    if cash >= coin_types[current_coin]:
                        cash -= coin_types[current_coin]
                        cash = round(cash, 2)
                        coins += 1
                    else:
                        current_coin += 1
                print(coins)
                exit(0)


main()
