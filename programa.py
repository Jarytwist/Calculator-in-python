#Impresiones de pantalla
def menu():
    print("Seleccione una opción:")
    print("1. Suma de n números")
    print("2. Producto entre n números")
    print("3. División entre 2 números")
    print("4. Calcular el factorial de n")
    print("5. Tablas de multiplicar")
    print("6. Cuadrado y cubo de un número")
    print("7. Promedio de una serie de números")
    print("8. Valores máximo y mínimo")
    print("9. Salir")

#Operaciones de suma
def suma_numeros():
    numeros = []
    while True:
        num = float(input("Ingrese un número (-1 para terminar): "))
        if num == -1:
            break
        numeros.append(num)
    print("La suma es:", sum(numeros))
