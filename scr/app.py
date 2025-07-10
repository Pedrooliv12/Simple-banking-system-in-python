import bank
from os import system, name

def clear_terminal():
    system('cls' if name == 'nt' else 'clear')

def show_menu():
    print("=== Simple Bank ===")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View extract")
    print("4. Exit")

def main():
    account = bank.Bank()
    while True:
        clear_terminal()
        show_menu()
        option = input("Choose an option: ")
        match option:
            case "1":
                clear_terminal()
                account.deposit()
                input("Press Enter to continue...")
            case "2":
                
                clear_terminal()
                account.withdraw()
                input("Press Enter to continue...")
            case "3":
                clear_terminal()
                account.view_extract()
                input("Press Enter to continue...")
            case "4":
                clear_terminal()
                print("Thank you for using the simple banking system!")
                break
            case _:
                clear_terminal()
                print("Invalid option. Please try again.")
                input("Press Enter to continue...")

if __name__ == "__main__":
    main()