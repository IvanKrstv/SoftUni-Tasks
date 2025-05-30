class MoneyNotEnoughError(Exception):
    pass

class PINCodeError(Exception):
    pass

class UnderageTransactionError(Exception):
    pass

class MoneyIsNegativeError(Exception):
    pass

def send_money(pin: str, bal: int, user_age: int,trans_info: str):
    money, current_pin = trans_info.split('#')[1:3]
    money = int(money)

    if money > bal:
        raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

    if pin != current_pin:
        raise PINCodeError("Invalid PIN code")

    if user_age < 18:
        raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

    bal -= money
    print(f"Successfully sent {money:.2f} money to a friend\n"
          f"There is {bal:.2f} money left in the bank account")

    return bal

def receive_money(bal: int, trans_info: str):
    money = int(trans_info.split('#')[1])

    if money < 0:
        raise MoneyIsNegativeError("The amount of money cannot be a negative number")
    print(f"{money/2:.2f} money went straight into the bank account")

    return bal + money

pin_code, balance, age = input().split(', ')
balance, age = int(balance), int(age)

while True:
    command = input()
    if command == 'End':
        break

    if command.startswith('Send Money'):
        balance = send_money(pin_code, balance, age, command)
    elif command.startswith('Receive Money'):
        balance = receive_money(balance, command)
