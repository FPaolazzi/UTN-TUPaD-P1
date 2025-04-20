#   Ejercicio 1:
edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad")


#   Ejercicio 2:
nota = int(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#   Ejercicio 3
numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
#   Ejercicio 4
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print ("Pertenece a la categoría de niño/a")
elif edad >= 12 and edad < 18:
    print ("Pertenece a la categoría de adolescente")
elif edad >= 18 and edad < 30:
    print ("Pertenece a la categoría de adulto/a joven")
else:
    print ("Pertenece a la categoría de adulto/a")
#   Ejercicio 5

contrasena = input("Ingrese una contraseña: ")

if len(contrasena) >= 8 and len(contrasena) <= 14:
    print ("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
#   Ejercicio 6

import random
import statistics

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
moda = statistics.mode(numeros_aleatorios)

print(f"Números aleatorios: {numeros_aleatorios}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("Sin sesgo (distribución simétrica)")
else:
    print("No se puede determinar un sesgo claro")

#   Ejercicio 7

frase = input("Escribí una palabra o frase: ")

ultima_letra = frase[-1].lower()

if ultima_letra in 'aeiou':
    frase += '!'
    
print(frase)


#   Ejercicio 8

nombre = input("Ingresá tu nombre: ")

print("Elegí una opción:")
print("1. Mostrar el nombre en mayúsculas")
print("2. Mostrar el nombre en minúsculas")
print("3. Mostrar el nombre con la primera letra en mayúscula")

opcion = input("Ingresá 1, 2 o 3: ")

if opcion == "1":
    print("Tu nombre en mayúsculas es:", nombre.upper())
elif opcion == "2":
    print("Tu nombre en minúsculas es:", nombre.lower())
elif opcion == "3":
    print("Tu nombre con la primera letra en mayúscula es:", nombre.title())
else:
    print("Opción no válida. Por favor ingresá 1, 2 o 3.")


#   Ejercicio 9

magnitud = int(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print ("Segun la escala de Richter: Muy leve (imperceptible).")
elif magnitud >= 3 and magnitud < 4:
    print ("Segun la escala de Richetr: Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud < 5:
    print ("Segun la escala de Richter: Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud >= 5 and magnitud < 6:
    print ("Segun la escala de Richter: Fuerte (puede causar daños en estructuras débiles).")
elif magnitud >= 6 and magnitud < 7:
    print ("Segun la escala de Richter: Muy fuerte (puede causar daños significativos).")
else:
    print ("Segun la escala de Richter: Extremo (puede causar graves daños a gran escala).")
#   Ejercicio 10

hemisferio = input("Ingrese el hemisferio en el cual se encuentra (N para norte y S para sur): ").strip().upper()
mes = int(input("Ingrese el mes del año en el que se encuentra (1-12): "))
dia = int(input("Ingrese el día del mes en el que se encuentra (1-31): "))

def obtener_estacion(mes, dia):
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        return "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        return "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        return "Verano"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        return "Otoño"

estacion_norte = obtener_estacion(mes, dia)

if hemisferio == "N":
    estacion = estacion_norte
elif hemisferio == "S":
    if estacion_norte == "Primavera":
        estacion = "Otoño"
    elif estacion_norte == "Verano":
        estacion = "Invierno"
    elif estacion_norte == "Otoño":
        estacion = "Primavera"
    elif estacion_norte == "Invierno":
        estacion = "Verano"
else:
    estacion = "Hemisferio no válido"

print("Estás en:", estacion)
