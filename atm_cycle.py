balance = 10000

while balance > 0:
    a = int(input("Enter the amount:"))

    if a > balance:
        print("You don't have that many :(")
    elif a > 0:
        balance = balance - a
        print(f"Your new balance: {balance}")
    else:
        print("The session has been deleted")
        break



    