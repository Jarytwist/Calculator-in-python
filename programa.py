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

#Operaciones de productos
def producto_numeros():
    numeros = []
    while True:
        num = float(input("Ingrese un número (-1 para terminar): "))
        if num == -1:
            break
        numeros.append(num)
    producto = 1
    for n in numeros:
        producto *= n
    print("El producto es:", producto)

# Operaciones de división
def division():
    num1 = float(input("Ingrese el numerador: "))
    num2 = float(input("Ingrese el denominador: "))
    if num2 != 0:
        print("El resultado de la división es:", num1 / num2)
    else:
        print("Error: División entre cero.")

# Operación factorial
def factorial(n):
    if n < 0:
        return "Error: No se puede calcular el factorial de un número negativo."
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

# Operación de tablas de multiplicación
def tablas_multiplicar():
    numero = int(input("Ingrese el número para la tabla de multiplicar: "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Operación de cuadrado y cubo
def cuadrado_cubo():
    num = float(input("Ingrese un número: "))
    print("El cuadrado es:", num ** 2)
    print("El cubo es:", num ** 3)

# OPeración de promedio
def promedio():
    numeros = []
    while True:
        num = float(input("Ingrese un número (-1 para terminar): "))
        if num == -1:
            break
        numeros.append(num)
    if len(numeros) > 0:
        print("El promedio es:", sum(numeros) / len(numeros))
    else:
        print("No se ingresaron números.")

# pOperación de maximo y minimo
def max_min():
    numeros = []
    while True:
        num = float(input("Ingrese un número (-1 para terminar): "))
        if num == -1:
            break
        numeros.append(num)
    if len(numeros) > 0:
        print("El valor máximo es:", max(numeros))
        print("El valor mínimo es:", min(numeros))
        print("Total de valores ingresados:", len(numeros))
    else:
        print("No se ingresaron números.")

#Función principal
def main():
    while True:
        menu()
        opcion = int(input("Ingrese su opción: "))
        if opcion == 1:
            suma_numeros()
        elif opcion == 2:
            producto_numeros()
        elif opcion == 3:
            division()
        elif opcion == 4:
            factorial()
        elif opcion == 5:
            tablas_multiplicar()
        elif opcion == 6:
            cuadrado_cubo()
        elif opcion == 7:
            promedio()
        elif opcion == 8:
            max_min()
        elif opcion == 9:
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

def main():
    while True:
        menu()
        opcion = int(input("Ingrese su opción: "))
        if opcion == 1:
            suma_numeros()
        elif opcion == 2:
            producto_numeros()
        elif opcion == 3:
            division()
        elif opcion == 4:
            factorial()
        elif opcion == 5:
            tablas_multiplicar()
        elif opcion == 6:
            cuadrado_cubo()
        elif opcion == 7:
            promedio()
        elif opcion == 8:
            max_min()
        elif opcion == 9:
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()