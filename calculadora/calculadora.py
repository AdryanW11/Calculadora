def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero."


memoria = 0

def armazenar_na_memoria(valor):
    global memoria
    memoria = valor
    print(f"Valor {valor} armazenado na memória.")

def usar_memoria():
    global memoria
    return memoria

def limpar_memoria():
    global memoria
    memoria = 0
    print("Memória limpa.")


def mostrar_menu():
    print("\nSelecione a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Armazenar na memória")
    print("6 - Usar valor da memória")
    print("7 - Limpar memória")
    print("8 - Sair")


def calculadora():
    while True:
        mostrar_menu()
        escolha = input("Digite sua escolha (1/2/3/4/5/6/7/8): ")

        if escolha in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                resultado = adicionar(num1, num2)
            elif escolha == '2':
                resultado = subtrair(num1, num2)
            elif escolha == '3':
                resultado = multiplicar(num1, num2)
            elif escolha == '4':
                resultado = dividir(num1, num2)

            print(f"Resultado: {resultado}")

        elif escolha == '5':
            valor = float(input("Digite o valor para armazenar na memória: "))
            armazenar_na_memoria(valor)

        elif escolha == '6':
            valor_memoria = usar_memoria()
            print(f"Valor armazenado na memória: {valor_memoria}")

        elif escolha == '7':
            limpar_memoria()

        elif escolha == '8':
            print("Saindo da calculadora...")
            break

        else:
            print("Opção inválida. Tente novamente.")


calculadora()
#bruh