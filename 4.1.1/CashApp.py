import json
import os

accounts_file = "stored.json"


def main():
    print("Welcome to Online Currency App!")
    print("1. Login")
    print("2. Create Account")
    print("3. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        login()
    elif choice == "2":
        create_account()
    elif choice == "3":
        quit()
    else:
        print("Invalid choice")
        main()

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == "admin" and password == "admin":
        admin_menu()
    elif os.path.exists(accounts_file):
        with open(accounts_file, "r") as f:
            accounts = json.load(f)
        if username in accounts and accounts[username]["password"] == password:
            user_menu(username)
        else:
            print("Invalid username or password")
            main()
    else:
        print("No accounts found")
        main()

def create_account():
    username = input("Enter a username: ")
    if os.path.exists(accounts_file):
        with open(accounts_file, "r") as f:
            accounts = json.load(f)
    else:
        accounts = {}
    if username in accounts:
        print("Username already exists")
        main()
    else:
        password = input("Enter a password: ")
        balance = float(input("Enter your initial balance: "))
        accounts[username] = {"password": password, "balance": balance}
        with open(accounts_file, "w") as f:
            json.dump(accounts, f)
        print("Account created successfully")
        login()

def user_menu(username):
    print("Welcome, {}!".format(username))
    print("Your balance is: ${accounts[user]}")
    print("1. Send Money")
    print("2. View Inbox")
    print("3. Logout")
    choice = input("Enter your choice: ")
    if choice == "1":
        send_money(username)
    elif choice == "2":
        view_inbox(username)
    elif choice == "3":
        main()
    else:
        print("Invalid choice")
        user_menu(username)

def send_money(username):
    with open(accounts_file, "r") as f:
        accounts = json.load(f)
    recipient = input("Enter the recipient's username: ")
    if recipient in accounts:
        amount = float(input("Enter the amount to send: "))
        if amount > accounts[username]["balance"]:
            print("Insufficient funds")
            user_menu(username)
        else:
            accounts[username]["balance"] -= amount
            accounts[recipient]["balance"] += amount
            with open(accounts_file, "w") as f:
                json.dump(accounts, f)
            print("Transaction successful")
            user_menu(username)
    else:
        print("Recipient not found")
        user_menu(username)

def view_inbox(username):
    with open(accounts_file, "r") as f:
        accounts = json.load(f)
    inbox = []
    for sender, data in accounts.items():
        if username in data.get("inbox", {}):
            inbox.append((sender, data["inbox"][username]))
    if inbox:
        print("You have the following transactions in your inbox:")
        for sender, amount in inbox:
            print("- {} sent you ${}".format(sender, amount))
            del accounts[sender]["inbox"][username]
        with open(accounts_file, "w") as f:
            json.dump(accounts, f)
    else:
        print("No transactions in your inbox")
    user_menu(username)

def admin_menu():
    print("Welcome, Admin!")
    print("1. Add Money to Account")
    print("2. Change Username")
    print("3. Change Balance")
    print("4. Logout")
    choice = input("Enter your choice: ")
    if choice == "1":
        username = input("Enter the username to add money to: ")
        if os.path.exists(accounts_file):
            with open(accounts_file, "r") as f:
                accounts = json.load(f)
            if username in accounts:
                amount = float(input("Enter the amount to add: "))
                accounts[username]["balance"] += amount
                with open(accounts_file, "w") as f:
                    json.dump(accounts, f)
                print("${} added to {}'s account".format(amount, username))
                admin_menu()
            else:
                print("User not found")
                admin_menu()
        else:
            print("No accounts found")
            admin_menu()
    elif choice == "2":
        username = input("Enter the current username: ")
        new_username = input("Enter the new username: ")
        if os.path.exists(accounts_file):
            with open(accounts_file, "r") as f:
                accounts = json.load(f)
            if username in accounts:
                accounts[new_username] = accounts.pop(username)
                with open(accounts_file, "w") as f:
                    json.dump(accounts, f)
                print("Username changed successfully")
                admin_menu()
            else:
                print("User not found")
                admin_menu()
        else:
            print("No accounts found")
            admin_menu()
    elif choice == "3":
        username = input("Enter the username: ")
        if os.path.exists(accounts_file):
            with open(accounts_file, "r") as f:
                accounts = json.load(f)
            if username in accounts:
                new_balance = float(input("Enter the new balance: "))
                accounts[username]["balance"] = new_balance
                with open(accounts_file, "w") as f:
                    json.dump(accounts, f)
                print("{}'s balance changed to ${}".format(username, new_balance))
                admin_menu()
            else:
                print("User not found")
                admin_menu()
        else:
            print("No accounts found")
            admin_menu()
    elif choice == "4":
        main()
    else:
        print("Invalid choice")
        admin_menu()

main()

   
