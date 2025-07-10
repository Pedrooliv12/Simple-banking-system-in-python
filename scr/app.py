import bank

def mostrar_menu():
    print("=== Banco Simples ===")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Ver saldo")
    print("4. Sair")

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1":
                bank.depositar()
            case "2":
                bank.sacar()
            case "3":
                bank.ver_saldo()
            case "4":
                print("Obrigado por usar o sistema bancário simples!")
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()