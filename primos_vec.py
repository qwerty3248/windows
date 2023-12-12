def Esprimo(n):
    primo = True
    for i in range(2, n - 1):
        if n % i == 0:
            primo = False
            return primo
    return primo

def main():
    tam = int(input("Introduzca la cantidad de numeros que va a querer comprobar que son primos: "))

    numeros = []  # una lista de numeros

    for i in range(tam):  # vamos a coger tam numeros
        numero = int(input("Introduzca numero para revisar si es primo: "))
        numeros.append(numero)

    for numero in numeros:
        if Esprimo(numero):
            print("El numero", numero, "es primo")
        else:
            print("El numero", numero, "NO es primo")

# la forma de definir un main en python basicamente es una funcion que se ejecuta
if __name__ == "__main__":
    main()

