### EJERICIO 1: Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el 
### factorial de todos los números enteros entre 1 y el número que indique el usuario
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un número entero positivo: "))

if numero < 1:
    print("¡Debe ingresar un número mayor o igual a 1!")
else:
    # Calcular y mostrar factoriales desde 1 hasta el número ingresado
    print("\nFactoriales desde 1 hasta", numero, ":")
    for i in range(1, numero + 1):
        print(f"{i}! = {factorial(i)}")


### EJERCICIO 2: Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie
### completa hasta la posición que el usuario especifique.
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

posicion = int(input("Ingrese un número entero positivo para la serie de Fibonacci: "))

if posicion < 1:
    print("¡Debe ingresar un número mayor o igual a 1!")
else:
    print("\nSerie de Fibonacci hasta la posición", posicion, ":")
    for i in range(posicion + 1):
        print(f"Posición {i}: {fibonacci(i)}")


### EJERCICIO 3: Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). 
### Prueba esta función en un algoritmo general.
def potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente < 0:
        return 1 / potencia(base, -exponente)
    else:
        return base * potencia(base, exponente - 1)

base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente (entero): "))

resultado = potencia(base, exponente)
print(f"\n{base} elevado a {exponente} es: {resultado}")


### EJERCICIO 4: Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario
###  como una cadena de texto.
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingrese un número entero positivo: "))

if numero < 0:
    print("¡Error! Debe ingresar un número positivo.")
else:
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")


### EJERCICIO 5: Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, 
### y devuelva True si es un palíndromo o False si no lo es. Requisitos:
### -    La solución debe ser recursiva.
### -    No se debe usar [::-1] ni la función reversed().
def es_palindromo(palabra, inicio=0, fin=None):
    if fin is None:
        fin = len(palabra) - 1
    
    if inicio >= fin:
        return True
    if palabra[inicio] != palabra[fin]:
        return False
    
    return es_palindromo(palabra, inicio + 1, fin - 1)

palabra_usuario = input("Ingrese una palabra (sin espacios ni tildes): ").strip().lower()
if es_palindromo(palabra_usuario):
    print(f"¡'{palabra_usuario}' es un palíndromo!")
else:
    print(f"'{palabra_usuario}' no es un palíndromo.")        


### EJERCICIO 6: Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
### Restricciones:
### -   No se puede convertir el número a string.
### -   Usá operaciones matemáticas (%, //) y recursión.
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

numero = int(input("Ingrese un número entero positivo: "))

if numero < 0:
    print("Error: Debe ingresar un número positivo.")
else:
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")


### EJERCICIO 7: Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), 
### y así sucesivamente hasta llegar al último nivel con un solo bloque. Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
### nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

try:
    bloques_base = int(input("Ingrese el número de bloques en la base de la pirámide: "))
    if bloques_base < 1:
        print("Error: Debe ingresar un número entero positivo.")
    else:
        total = contar_bloques(bloques_base)
        print(f"Se necesitan {total} bloques para construir la pirámide.")
except ValueError:
    print("Error: Ingrese solo números enteros.")


### EJERCICIO 8: Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), 
### y devuelva cuántas veces aparece ese dígito dentro del número.
def contar_digito(numero, digito):
    if numero < 10:
        return 1 if numero == digito else 0
    else:
        ultimo_digito = numero % 10
        return (1 if ultimo_digito == digito else 0) + contar_digito(numero // 10, digito)

try:
    numero = int(input("Ingrese un número entero positivo: "))
    digito = int(input("Ingrese un dígito (0-9) a buscar: "))
    
    if numero < 0:
        print("Error: El número debe ser positivo.")
    elif digito < 0 or digito > 9:
        print("Error: El dígito debe estar entre 0 y 9.")
    else:
        cantidad = contar_digito(numero, digito)
        print(f"El dígito {digito} aparece {cantidad} veces en el número {numero}.")
except ValueError:
    print("Error: Ingrese solo valores numéricos enteros.")