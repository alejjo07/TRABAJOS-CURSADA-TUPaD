import os
os.system("cls")

#ACTIVIDADES

#------------------------------------------------

#EJERCICIO 1

#precio_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
#1450}

#precio_frutas ["Naranja"] = 1200
#precio_frutas ["Manzana"] = 1500
#precio_frutas ["Pera"] = 2300

#print(precio_frutas)

#------------------------------------------------

#EJERCICIO 2

#precio_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
#1450}

#precio_frutas ["Naranja"] = 1200
#precio_frutas ["Manzana"] = 1500
#precio_frutas ["Pera"] = 2300

#precio_frutas ["Banana"] = 1330
#precio_frutas ["Manzana"] = 1700
#precio_frutas ["Melon"] = 2800

#print(precio_frutas)

#------------------------------------------------

#EJERCICIO 3

#precio_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
#1450}

#precio_frutas ["Naranja"] = 1200
#precio_frutas ["Manzana"] = 1500
#precio_frutas ["Pera"] = 2300

#precio_frutas ["Banana"] = 1330
#precio_frutas ["Manzana"] = 1700
#precio_frutas ["Melon"] = 2800

#solo_frutas = list(precio_frutas.keys())

#print(solo_frutas)

#------------------------------------------------

#EJERCICIO 4

#contactos = {"Juan":48392,
#             "Pedro":71503,
#             "Alejo":20984,
#             "Bruno":69417,
#             "Maxi":35761 
#}

#nombre = input("Ingrese alguno de los siguientes nombres - Juan, Pedro, Alejo, Bruno, Maxi: ")

#if nombre in contactos:
#    print(f"El número de {nombre} es: {contactos[nombre]}")

#else:
#    print("Ese contacto no está en la agenda. Verifique el nombre ingresado.")

#------------------------------------------------

#EJERCICIO 5

#frase = input("Ingrese una frase: ")
#palabras = frase.split()

#palabras_unicas = set(palabras)

#print("Palabras que son unicas: ",palabras_unicas)

#------------------------------------------------

#EJERCICIO 6
#alumnos = {}
#for i in range(1, 4):
#    nombre = input(f"Ingrese el nombre del alumno {i}: ")
#    notas = []
#    for j in range(1, 4):
#        nota = int(input(f"Ingrese la nota {j} de {nombre}: "))
#        notas.append(nota)
#    alumnos[nombre] = notas

#for nombre, notas in alumnos.items():
#    promedio = sum(notas) / len(notas)
#    print(f"El promedio de {nombre} es: {promedio:.2f}")

#------------------------------------------------

#EJERCICIO 7

#parcial1 = input("Ingrese los nombres de los alumnos que aprobaron el primer parical (separados por coma):  ")
#parcial2 = input("Ingrese los nombres de los alumnos que aprobaron el segundo parcial (separados por coma):  ")

#parcial1 = {}
#parcial2 = {}

#ambos = parcial1 & parcial2 

#soloamente_un_parcial = parcial1 ^ parcial2 

#al_menos_un_parcial = parcial1 | parcial2

#print("Alumnos que aprobaron ambos parciales:", ambos)
#print("Alumnos que aprobaron solo un parcial:", soloamente_un_parcial)
#print("Alumnos que aprobaron al menos un parcial:", al_menos_un_parcial)

#------------------------------------------------

#EJERCICIO 8

#consulta = input("Ingrese el producto que desea consultar: ")

#stock_productos = {
#    "Manzana": 10,
#    "Banana": 5,
#    "Pera": 8
#}

#if consulta in stock_productos:
#    print(f"Hay {stock_productos[consulta]} unidades de {consulta} en stock.")
#    agregar = int(input("¿Cuántas unidades desea agregar? "))
#    stock_productos[consulta] += agregar
#    print(f"Nuevo stock de {consulta}: {stock_productos[consulta]}")
#else:
#    stock_productos[consulta] = 0 
#    print(stock_productos[consulta])

#------------------------------------------------

#EJERCICIO 9

#dia = input("Ingrese el dia de la semana que desee: ").strip().capitalize()
#hora = input("Ingrese la hora que desee (ej: 10:00 AM): ").strip().upper()

#agenda = {
#    ("Lunes", "10:00 AM"): "Reunión con el equipo de marketing",
#    ("Martes", "2:00 PM"): "Cita médica",
#    ("Miércoles", "11:30 AM"): "Reunión con el cliente",
#}

#clave = (dia, hora)
#if clave in agenda:
#    print(f"El evento programado para {dia} a las {hora} es: {agenda[clave]}")
#else:
#    print("No hay evento programado para ese día y hora.")
#    nuevo_evento = input("¿Desea agregar un evento? (si/no): ").strip().lower()
#    if nuevo_evento == "si":
#        descripcion = input("Ingrese la descripción del evento: ")
#        agenda[clave] = descripcion
#        print("Evento agregado correctamente.")

#------------------------------------------------

#EJERCICIO 10

#original = {"Argentina": "Buenos Aires",
#           "Brasil": "Brasilia",
#           "Chile": "Santiago",
#           "Colombia": "Bogotá",}

#invertido = {"Buenos Aires": "Argentina",
#            "Brasilia": "Brasil",
#            "Santiago": "Chile",
#            "Bogotá": "Colombia",}

#------------------------------------------------