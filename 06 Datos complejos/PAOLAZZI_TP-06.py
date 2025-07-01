## Ejercicio 1:  Dado el diccionario precios_frutas
##              precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
##              Añadir las siguientes frutas con sus respectivos precios:
##                  ● Naranja = 1200
##                  ● Manzana = 1500
##                  ● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)


## Ejercicio 2: Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
##              desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
##                  ● Banana = 1330
##                  ● Manzana = 1700
##                  ● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)


## Ejercicio 3: Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
##              desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

lista_frutas = list(precios_frutas.keys())

print(lista_frutas)


## Ejercicio 4: Escribí un programa que permita almacenar y consultar números telefónicos.
##              • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
##              • Luego, pedí un nombre y mostrale el número asociado, si existe.

agenda = {}

for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto #{i+1}: ")
    numero = input(f"Ingresá el número de teléfono de {nombre}: ")
    agenda[nombre] = numero

consulta = input("Ingresá el nombre del contacto que querés buscar: ")

if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print(f"No se encontró ningún contacto con el nombre '{consulta}'.")


## Ejercicio 5: Solicita al usuario una frase e imprime:
##              • Las palabras únicas (usando un set).
##              • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingresá una frase: ")

frase = frase.lower()

palabras = frase.split()

palabras_unicas = set(palabras)

recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("\nPalabras_únicas:", palabras_unicas)
print("Recuento:", recuento)


## Ejercicio 6: Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
##              Luego, mostrá el promedio de cada alumno.

alumnos = {}

for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno #{i+1}: ")
    print(f"Ingresá las 3 notas de {nombre}:")
    
    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 2: "))
    nota3 = int(input("Nota 3: "))
    
    alumnos[nombre] = (nota1, nota2, nota3)

print("\nPromedios:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")


## Ejercicio 7: Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
##              y Parcial 2:
##              • Mostrá los que aprobaron ambos parciales.
##              • Mostrá los que aprobaron solo uno de los dos.
##              • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {'Flor', 'Cristian', 'Silvia', 'Miguel'}
parcial2 = {'Luis', 'Miguel', 'Julián', 'Silvia'}

ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los dos:", solo_uno)

al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)


## Ejercicio 8: Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
##              Permití al usuario:
##              • Consultar el stock de un producto ingresado.
##              • Agregar unidades al stock si el producto ya existe.
##              • Agregar un nuevo producto si no existe

stock_productos = {
    "pan": 20,
    "leche": 15,
    "huevos": 30
}

print("Stock inicial:", stock_productos)

producto = input("\nIngresá el nombre de un producto: ").lower()

if producto in stock_productos:
    print(f"Stock actual de {producto}: {stock_productos[producto]}")
    agregar = input("¿Querés agregar unidades a este producto? (s/n): ").lower()
    if agregar == 's':
        cantidad = int(input("¿Cuántas unidades querés agregar?: "))
        stock_productos[producto] += cantidad
        print(f"Nuevo stock de {producto}: {stock_productos[producto]}")
else:
    print(f"{producto} no existe en el inventario.")
    agregar_nuevo = input("¿Querés agregarlo como nuevo producto? (s/n): ").lower()
    if agregar_nuevo == 's':
        cantidad = int(input("¿Cuántas unidades tiene?: "))
        stock_productos[producto] = cantidad
        print(f"{producto} fue agregado con {cantidad} unidades.")

print("\nStock actualizado:")
print(stock_productos)


## Ejercicio 9: Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:30"): "Entrenamiento",
    ("jueves", "14:00"): "Almuerzo con cliente",
    ("viernes", "16:45"): "Revisión de proyectos"
}

def consultar_evento(dia, hora):
    return agenda.get((dia.lower(), hora), "No hay eventos programados para ese día y hora")

print(consultar_evento("lunes", "10:00"))
print(consultar_evento("sábado", "12:00"))


## Ejercicio 10: Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
##              diccionario donde:
##              • Las capitales sean las claves.
##              • Los países sean los valores.
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo",
    "Colombia": "Bogotá"
}

# Método 1: Usando comprensión de diccionarios
invertido = {capital: pais for pais, capital in original.items()}

print("Diccionario original:", original)
print("Diccionario invertido:", invertido)
