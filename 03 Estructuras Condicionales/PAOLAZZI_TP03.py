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
    # Cambiamos la estación a la opuesta
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