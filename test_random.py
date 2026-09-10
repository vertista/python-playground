import random
import time

print("You've entered the bunker!")
time.sleep(1)

number = random.randint(1,5)
f = 100
d = 0

while True:
    
    print("Guess a number between 1 and 5!")
    try:
        a = int(input())
        if a == number:
            print("You guessed it—you've successfully made it into the bunker!")
            break
    except ValueError:
        print("Enter numbers, not letters")
    continue

while True:
    food = random.randint(10, 25)
    d += 1
    f = f - food
    print(f"Day {d}")
    print(f"You have {f} food!")
    time.sleep(0.5)

    if f <= 0:
        print(f"We're out of food! You've lasted {d} days.")
        break
    elif d == 5:
        print("You've made it to spring! Victory!")
        break


    print("--- Menu ---")
    print("1. Continue")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        continue
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Wrong input! Please enter 1 or 2.")

