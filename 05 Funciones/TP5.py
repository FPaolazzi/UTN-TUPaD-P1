### 1: Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.
 
# --- DEFINICIÓN DE FUNCIONES ---

def imprimir_hola_mundo():
    """Imprime el mensaje 'Hola Mundo!' en pantalla."""
    print("Hola Mundo!")

# --- PROGRAMA PRINCIPAL ---

if __name__ == "__main__":
    imprimir_hola_mundo()


### 2: Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
### Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
### principal solicitando el nombre al usuario.

 # --- DEFINICIÓN DE FUNCIONES ---

def saludar_usuario(nombre):
    """Devuelve un saludo personalizado para el nombre dado."""
    return f"Hola {nombre}!"

# --- PROGRAMA PRINCIPAL ---

if __name__ == "__main__":
    nombre_ingresado = input("Ingrese su nombre: ")
    saludo = saludar_usuario(nombre_ingresado)
    print(saludo)


### 3: Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy
### [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# --- DEFINICIÓN DE FUNCIONES ---

def informacion_personal(nombre, apellido, edad, residencia):
    """Imprime una frase con los datos personales ingresados."""
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# --- PROGRAMA PRINCIPAL ---

if __name__ == "__main__":
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    residencia = input("Ingrese su lugar de residencia: ")

    informacion_personal(nombre, apellido, edad, residencia)


### 4: Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_
### circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
### funciones para mostrar los resultados.

import math

# --- DEFINICIÓN DE FUNCIONES ---

def calcular_area_circulo(radio):
    """Devuelve el área de un círculo dado su radio."""
    return math.pi * radio**2

def calcular_perimetro_circulo(radio):
    """Devuelve el perímetro (circunferencia) de un círculo dado su radio."""
    return 2 * math.pi * radio

# --- PROGRAMA PRINCIPAL ---

if __name__ == "__main__":
    radio = float(input("Ingrese el radio del círculo: "))

    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)

    print(f"Área del círculo: {area:.2f}")
    print(f"Perímetro del círculo: {perimetro:.2f}")


### 5: Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad
### de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# --- DEFINICIÓN DE FUNCIONES ---

def segundos_a_horas(segundos):
    """Convierte una cantidad de segundos a horas."""
    return segundos / 3600

# --- PROGRAMA PRINCIPAL ---

if __name__ == "__main__":
    segundos_ingresados = int(input("Ingrese la cantidad de segundos: "))
    horas = segundos_a_horas(segundos_ingresados)
    print(f"{segundos_ingresados} segundos equivalen a {horas:.2f} horas.")


### 6: Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese
### número del 1 al 10. Pedir al usuario el número y llamar a la función.

# --- DEFINICIÓN DE FUNCIONES ---

def tabla_multiplicar(numero):
    """Imprime la tabla de multiplicar del 1 al 10 para el número dado."""
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# --- PROGRAMA PRINCIPAL ---

if __name__ == "__main__":
    numero_usuario = int(input("Ingrese un número: "))
    tabla_multiplicar(numero_usuario)


### 7: Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado
### de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

# --- DEFINICIÓN DE FUNCIONES ---

def operaciones_basicas(a, b):
    """
    Devuelve una tupla con la suma, resta, multiplicación y división de a y b.
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinida (división por cero)"
    return (suma, resta, multiplicacion, division)

# --- PROGRAMA PRINCIPAL ---

if __name__ == "__main__":
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    resultados = operaciones_basicas(num1, num2)

    print("\nResultados de las operaciones:")
    print(f"Suma: {resultados[0]}")
    print(f"Resta: {resultados[1]}")
    print(f"Multiplicación: {resultados[2]}")
    print(f"División: {resultados[3]}")


### 8: Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de
### masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

# --- DEFINICIÓN DE FUNCIONES ---

def calcular_imc(peso, altura):
    """Calcula y devuelve el índice de masa corporal (IMC)."""
    return peso / (altura ** 2)

# --- PROGRAMA PRINCIPAL ---

if __name__ == "__main__":
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))

    imc = calcular_imc(peso, altura)
    print(f"Su IMC es: {imc:.2f}")


### 9: Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en
### Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.
 
# --- DEFINICIÓN DE FUNCIONES ---

def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit y devuelve el resultado."""
    return (9/5) * celsius + 32

# --- PROGRAMA PRINCIPAL ---

if __name__ == "__main__":
    temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
    print(f"{temperatura_celsius}°C equivalen a {temperatura_fahrenheit:.2f}°F")


### 10: Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
### Solicitar los números al usuario y mostrar el resultado usando esta función.

# --- DEFINICIÓN DE FUNCIONES ---

def calcular_promedio(a, b, c):
    """Devuelve el promedio de tres números."""
    return (a + b + c) / 3

# --- PROGRAMA PRINCIPAL ---

if __name__ == "__main__":
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))

    promedio = calcular_promedio(num1, num2, num3)
    print(f"El promedio es: {promedio:.2f}")