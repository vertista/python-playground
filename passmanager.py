import time

password = input("Your password:")
creation_time = time.ctime()
miss = 0
MAX_ERRORS = 3


while True:
    print("\n--- Your menu ---")
    print("1. See your password")
    print("2. When your password was created")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        print(f"Your password is {password}")
        time.sleep(0.5)
    elif choice == "2":
        print(f"Your password was created at: {creation_time}")
        time.sleep(0.5)
    elif choice == "3":
        print("You have logged out. Goodbye!")
        break
    else:
        miss += 1

        remaining_attempts = MAX_ERRORS - miss
        
        if remaining_attempts > 0:
            print(f"Wrong input! You have {remaining_attempts} attempts left before session termination.")
            time.sleep(0.5)
        else:
            print("The session has been terminated due to too many mistakes.")
            break
            
