def crear_matriz(filas, columnas):
    # Crea una matriz con ceros
    matriz = [[0] * columnas for _ in range(filas)] #Es crea un [0] tantas columnas y lo hace eso filas
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:#no hace falta tamaño porque python maneja el tamaño de las lista automaticamente es decir de la lista de columas*filas
        print(fila)

def llenar_matriz(matriz):
    for i in range(len(matriz)):#ahora se una len para saber cuantas filas tiene, saca cuantas filas tiene 
        for j in range(len(matriz[0])):#aqui esta el 0 porque todas las filas tienen las mismas columnas por eso len saca cuantas columnas
            valor = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))#con el {i} se pinta la i, lo mismo con la j
            matriz[i][j] = valor

def main():
    # Solicita al usuario el tamaño de la matriz
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))

    # Crea una matriz con el tamaño proporcionado por el usuario
    matriz = crear_matriz(filas, columnas)

    # Llena la matriz con valores ingresados por el usuario
    llenar_matriz(matriz)

    # Imprime la matriz resultante
    imprimir_matriz(matriz)

if __name__ == "__main__":
    main()


