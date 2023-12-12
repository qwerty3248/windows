

def Esprimo (n):

    primo = True
    for i in range(2 , n-1):
        if n % i == 0:
            primo = False
            return primo
        #elif condicion:
        #else: 
        #asi es como continuaria con más condiciones el if en python
    return primo

numero_str = input ("Introduzca un numero para comprobar si es par o impar: ")
numero_entero =   int(numero_str)#convertimos la entrada a un entero  

if Esprimo(numero_entero):
    print("El numero ",numero_entero," es primo")
else:
    print("El numero ",numero_entero," NO es primo")


