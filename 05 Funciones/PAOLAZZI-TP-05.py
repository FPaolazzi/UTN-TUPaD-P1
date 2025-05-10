# Ejercicio 1: 

multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)


# Ejercicio 2: 

muebles = ['Mesa', 'Silla', 'Sillon', 'Cama', 'Escritorio']

print(muebles[3])


# Ejercicio 3: 

mi_lista = []

mi_lista.append("Python")
mi_lista.append("Programación")
mi_lista.append("VS Code")

print(mi_lista)


# Ejercicio 4:

animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"

animales[3] = "oso"

print(animales)


# Ejercicio 5:

numeros = [8, 5, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# Lo que está pasando en este ejemplo es que con la funcion remove se eliminó el numero más grande, es decir, el valor máximo.


# Ejercicio 6: Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

lista = list(range(10, 31, 5))

print("Los dos primeros elementos son:", lista[:2])


# Ejercicio 7: Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.

autos = ["sedan", "polo", "suran", "gol"]

autos[1:3] = ["clio", "march"]

print("Lista actualizada:", autos)


#  Ejercicio 8: Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. 
# Imprimir la lista resultante por pantalla.

dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print("Lista resultante:", dobles)


# Ejercicio 9: Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
#   a) Agregar "jugo" a la lista del tercer cliente usando append.
#   b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#   c) Eliminar "pan" de la lista del primer cliente.
#   d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")

indice_fideos = compras[1].index("fideos")
compras[1][indice_fideos] = "tallarines"

compras[0].remove("pan")

print("Lista resultante:", compras)


# Ejercicio 10: Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#   ● Posición lista_anidada[0]: 15
#   ● Posición lista_anidada[1]: True
#   ● Posición lista_anidada[2][0]: 25.5
#   ● Posición lista_anidada[2][1]: 57.9
#   ● Posición lista_anidada[2][2]: 30.6
#   ● Posición lista_anidada[3]: False
#   Imprimir la lista resultante por pantalla.

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print (lista_anidada)