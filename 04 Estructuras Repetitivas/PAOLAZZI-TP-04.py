# Ejercicio 1: Crea un programa que imprima en pantalla todos los numeros enteros desde 0 hasta 100, en orden creciente,
#              mostrando un numero por linea.

for i in range (101):
    print (i)


# Ejercicio 2: Desarrolla un programa que solicite al usuario un numero entero y determine la cantidad de digitos que contiene.

numero = int(input("Ingresa un número entero: "))
contador = 0

if numero == 0:
    contador = 1
else:
    temp = abs(numero)
    while temp > 0:
        temp = temp // 10
        contador += 1

print(f"El número {numero} tiene {contador} dígito(s).")


# Ejercicio 3: Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario,
#              excluyendo esos dos valores.

inicio = int(input("Ingresa el primer número entero: "))
fin = int(input("Ingresa el segundo número entero: "))

suma = 0

rango = range(inicio + 1, fin) if inicio < fin else range(fin + 1, inicio)

for num in rango:
    suma += num

print(f"La suma de los números entre {inicio} y {fin} (excluyéndolos) es: {suma}")


# Ejercicio 4: Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe
#              detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

total = 0
continuar = True

print("Ingresa números enteros para sumar. Ingresa 0 para finalizar.")

while continuar:
    numero = int(input("Número: "))
    if numero == 0:
        continuar = False
    else:
        total += numero

print(f"El total acumulado es: {total}")


# Ejercicio 5: Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe
#              mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numero_secreto = random.randint(0, 9)
intentos = 0
intento = -1

print("¡Adivina el número secreto entre 0 y 9!")

while intento != numero_secreto:
    intento = int(input("Tu intento: "))
    intentos += 1
    
    if intento != numero_secreto:
        print("Incorrecto. Intenta nuevamente.")

print(f"¡Correcto! El número era {numero_secreto}.")
print(f"Necesitaste {intentos} intento(s).")


# Ejercicio 6: Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for numero in range(100, -1, -2):
    print(numero)


# Ejercicio 7: Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

n = int(input("Ingresa un número entero positivo: "))

if n < 0:
    print("Error: Debes ingresar un número positivo.")
else:
    suma = 0
    for numero in range(n + 1):
        suma += numero

    print(f"La suma de los números desde 0 hasta {n} es: {suma}")


# Ejercicio 8: Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números 
#              son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una 
#              cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares = 0
impares = 0
positivos = 0
negativos = 0

print("Ingresa 100 números enteros:")

contador = 0
while contador < 100:
    entrada = input(f"Número {contador + 1}: ")
    
    numero_valido = 1
    posicion = 0
    while posicion < len(entrada):
        caracter = entrada[posicion]
        if not (posicion == 0 and caracter == '-'):
            if caracter not in '0123456789':
                numero_valido = 0
        posicion += 1
    
    if numero_valido == 1 and entrada not in ['', '-']:
        numero = int(entrada)
        contador += 1
        
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
        
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
    else:
        print("Error: Ingresa solo números enteros")

print("\nResultados:")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")


# Ejercicio 9: Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. 
#              (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

CANTIDAD_NUMEROS = 100

suma_total = 0
contador = 0

print(f"Ingresa {CANTIDAD_NUMEROS} números enteros:")

while contador < CANTIDAD_NUMEROS:
    entrada = input(f"Número {contador + 1}: ")
    
    es_valido = 1
    for caracter in entrada:
        if caracter not in '-0123456789':
            es_valido = 0
    
    if es_valido and entrada not in ['', '-']:
        numero = int(entrada)
        suma_total += numero
        contador += 1
    else:
        print("Error: Debe ser un número entero válido.")

media = suma_total / CANTIDAD_NUMEROS
print(f"\nLa media de los {CANTIDAD_NUMEROS} números es: {media:.2f}")


# Ejercicio 10: Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. 
#               Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingresa un número entero positivo: ")

if numero.isdigit():
    numero_invertido = numero[::-1]
    print(f"El número invertido es: {numero_invertido}")
else:
    print("Error: Debes ingresar un número entero positivo.")