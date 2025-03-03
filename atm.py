print("Welcome to the ATM!")

usrnme = "Anas Hussain"
pin = 1908
balance = 1000

ask_pin = int(input("Enter your pin: "))
if ask_pin != pin:
    print("Wrong pin!")
    exit()

print("Correct pin!")
print("Welcome 'Anas Hussain' ")

def withdrawal(amount):
    global balance 
    if amount <= balance:
        balance -= amount
        return "Amount withdrawn!"
    else:
        return "Insufficiant funds!"

def deposit(amount):
    global balance 
    balance += amount
    return "Amount deposited!"

def check_balance():
    global balance
    return f"Your balance: {balance}"


def ATM():
    while True:

        
        print("Options: ")
        print("1) Deposit.")
        print("2) Withdrawal.")
        print("3) Check your balance.")
        
        choice = (input("Enter your choice (1/2/3): "))

        if choice == '1':
            amount = ((int(input("Enter the amount you want to deposit: "))))
            print (deposit(amount))
        
        elif choice == '2':
            amount = (((int(input("Enter the amount you want to withdraw: ")))))
            print(withdrawal(amount))

        elif choice == '3':
            print (check_balance())
        
        else:
            print("Invalid option!")

        if not ask_again():
            break

def ask_again():
    choice = input ("Want to perform another task? (yes/no): ").strip().lower()
    return choice == "yes"

ATM()