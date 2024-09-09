#Metodo Somar
def somar(x, y):
    return x + y

#Metodo Subtrair
def subtrair(x, y):
    return x - y

#Metodo Multiplicar
def multiplicar(x, y):
    return x * y

#Metodo Dividir
def dividir(x, y):
    if y == 0:
        raise ValueError("Não é possível dividir por zero!")
    return x / y