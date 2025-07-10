import bank

def show_menu():
    print("=== Simple Bank ===")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View extract")
    print("4. Exit")

def main():
    account = bank.Bank()
    while True:
        show_menu()
        option = input("Choose an option: ")
        match option:
            case "1":
                account.deposit()
            case "2":
                account.withdraw()
            case "3":
                account.view_extract()
            case "4":
                print("Thank you for using the simple banking system!")
                break
            case _:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()