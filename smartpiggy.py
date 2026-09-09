balance = 0

while True:
    amount = int(input("Enter the amount:"))

    if amount > 0:
        balance = balance + amount
        print(f"Added!{amount} Current balance: {balance}!")
    else:
        print(f"The piggy bank is closed. Total amount: {balance}")
        break