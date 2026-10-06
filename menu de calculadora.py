def somar(a, b):
    return a + b
def subtrair(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b == 0:
        return "Erro!, divisao por zero"
    return a / b

while True:
    print("\n ---MENU---")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "5":
        print("Saindo...")
        break

    if opcao not in ["1", "2", "3", "4"]:
        print("Opcao invalida")
        continue
    numero1 = float(input("Numero 1: "))
    numero2 = float(input("Numero 2: "))
    if opcao == "1":
        print(f"Resultado: {somar(numero1, numero2)}")
    elif opcao == "2":
        print(f"Resultado: {subtrair(numero1,numero2)}")
    elif opcao == "3":
        print(f"Resultado: {multiplicar(numero1, numero2)}")
    elif opcao == "4":
        print(f"Resultado: {dividir(numero1, numero2)}")





