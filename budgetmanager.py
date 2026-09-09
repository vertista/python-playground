import time

while True:
    try:
        amount = int(input("Enter the amount:"))
        time.sleep(0.3)
        break
    except ValueError:
        print("Please type a number, not letters!")
        time.sleep(0.3)
    continue

time.sleep(0.3)
print(f"Your balance is {amount}!")

while True:
    try:
        price = int(input("Enter the amount:"))
        time.sleep(0.3)
    except ValueError:
        print("Please type a number, not letters!")
        time.sleep(0.3)
        continue
    if price <= amount:
        amount = amount - price
        print(f"Your new balance is {amount}")
        time.sleep(0.3)
    else:
        print("You don't have enough money")
        time.sleep(0.3)
        continue
    

