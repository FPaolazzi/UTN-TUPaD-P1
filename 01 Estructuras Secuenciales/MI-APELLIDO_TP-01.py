# Ejercicio 1
print ("Hola Mundo!")

# Ejercicio 2
nombre = input ("Ingrese su nombre:")

print (f"Hola {nombre}!")

# Ejercicio 3
nombre = input("Ingrese su nombre: ")

apellido = input("Ingrese su apellido: ")

edad = input ("Ingrese su edad: ")

residencia = input("Indique su lugar de residencia: ")

print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Ejercicio 4
radio = float (input ("Ingrese el radio del circulo: "))
perimetro = (2 * 3.14159 * radio)

print (f"El radio es: {radio}")
print (f"El perimetro es: {perimetro}")

# Ejercicio 5
segundos = float (input ("Indique la cantidad de segundos: "))
horas = (segundos / 60 / 60) 

print (f"{segundos} segundos equivalen a {horas} horas.")

# Ejercicio 6
num = int (input ("Ingrese un numero: "))

print(f"{num} x 1 = {num * 1}")
print(f"{num} x 2 = {num * 2}")
print(f"{num} x 3 = {num * 3}")
print(f"{num} x 4 = {num * 4}")
print(f"{num} x 5 = {num * 5}")
print(f"{num} x 6 = {num * 6}")
print(f"{num} x 7 = {num * 7}")
print(f"{num} x 8 = {num * 8}")
print(f"{num} x 9 = {num * 9}")
print(f"{num} x 10 = {num * 10}")

# Ejercicio 7
num1 = float (input ("Ingrese el primer numero: "))
num2 = float (input ("Ingrtese el segundo numero: "))

suma = num1 + num2
divid = num1 / num2
multip = num1 * num2
rest = num1 - num2

print (f"La suma de {num1} y {num2} es {suma}, la division es {divid}, la multiplicacion es {multip}, y la resta es {rest}.")

# Ejercicio 8
altura = float(input("Ingrese su altura en metros: "))
peso = float (input ("Ingrese su peso en kilogramos: "))

IMC = peso / (altura * altura)

print (f"Su indice de masa corporal es {IMC}.")

# Ejercicio 9
cels = float (input ("Ingrese la temperatura en grados Celsius: "))

farenh = (( 9 / 5) * cels) + 32

print (f"La temperatura en grados Farenheit es de {farenh}.")

# Ejercicio 10
num1 = float (input ("Ingrese el primer numero: "))
num2 = float (input ("Ingrese el segundo numero: "))
num3 = float (input ("Ingrese el tercer numero: "))

promed = (num1 + num2 + num3) / 3

print (f"El promedio de los tres numeros es: {promed}.")
