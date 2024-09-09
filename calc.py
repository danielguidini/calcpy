#Metodo Somar
def soma(x, y):
    return x + y

#Metodo Subtrair
def sub(x, y):
    return x - y

#Metodo Multiplicar
def mult(x, y):
    return x * y

#Metodo Dividir
def div(x, y):
    if y == 0:
        raise ValueError("Não é possível dividir por zero!")
    return x / y

#Programa Principal
def calculadora():
    while True:
        print()
        print("Selecione uma operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        print()

        #Escolha da Operação pelo usuario
        escolha = input("Digite sua escolha: ")
        print()
        
        #Escape do loop e encerramento do programa
        if escolha == '5':
            break
        
        #Inserção dos dados pelo o usuario
        num1 = float(input("Digite o primeiro número: "))
        print()
        num2 = float(input("Digite o segundo número: "))
        print()

        #Estrutura Condicional da escolha do usuario
        if escolha == '1':
            print("Resultado:", soma(num1, num2))
        elif escolha == '2':
            print("Resultado:", sub(num1, num2))
        elif escolha == '3':
            print("Resultado:", mult(num1, num2))
        elif escolha == '4':
            print("Resultado:", div(num1, num2))
        else:
            print("Escolha inválida. Tente novamente.")
        print()

#Chama a função para usar a calculadora
calculadora()