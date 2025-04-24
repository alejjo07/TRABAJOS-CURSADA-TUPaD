import os
os.system("cls")

#ACTIVIDAD 1
#edad = int(input("Introduzca su edad: "))

#if edad >= 18:
#    print("Usted es mayor de edad.")

#--------------------------------------------------#
#ACTIVIDAD 2

#nota = int(input("Introduzca su nota: "))

#if nota >= 6:
#   print("Aprobado.")
#else:
#    print("Desaprobado.")

#--------------------------------------------------#
#ACTIVIDAD 3

#numero = int(input("Introduzca un numero par: "))

#if numero % 2 == 0:
#    print("Ha ingresado un numero par.")
#else:
#    print("Por favor ingrese un numero par.")

#--------------------------------------------------#
#ACTIVIDAD 4

#edad = int(input("Ingrese su edad: "))

#if edad < 12:
#    print("Categoria: Menor.")
#elif edad >= 12 and edad < 18:
#    print("Categoria: Adolescente.")
#elif edad >= 18 and edad < 30:
#    print("Categoria: Adulto joven.")
#elif edad >= 30:
#    print("Categoria: Adulto.")

#--------------------------------------------------#
#ACTIVIDAD 5
#contraseña = input("Ingrese una contraseña entre 8 y 14 caracteres: ")

#if len(contraseña) >= 8 and len(contraseña) <= 14:
#    print("Ha ingresado una contraseña correcta.")
#else:
#    print("Ingrese una contraseña de entre 8 y 14 caracteres.")

#--------------------------------------------------#
#ACTIVIDAD 6
#import random
#from statistics import mode, median, mean 
#numeros_aleatorios = [random.randint(1, 100) for i in range (50)]

#media = mean (numeros_aleatorios)
#mediana = median (numeros_aleatorios)
#moda = mode (numeros_aleatorios)

#print("Lista de numeros aleatorios: ", numeros_aleatorios)
#print("Media: ", media)
#print("Median: ", mediana)
#print("Moda: ", moda)

#if media > mediana and mediana > moda:
#    print("La distribucion tiene sesgo positivo (a la derecha).")
#elif media < mediana and mediana < moda:
#    print("La distribución tiene sesgo negativo (a la izquierda).")
#elif media == mediana == moda:
#    print("La distribución no tiene sesgo.")
#else:
#    print("La distribución no cumple con los patrones de sesgo definidos.")

#--------------------------------------------------#
#ACTIVIDAD 7
#palabra = input("Introduzca una frase o palabra: ").lower()

#if palabra.endswith(("a", "e", "i", "o", "u")):
#    print(palabra + "!")
#else:
#    print(palabra)

#--------------------------------------------------#
#ACTIVIDAD 8
#nombre = input("Ingrese su nombre: ")
#print("------------------------------")
#print("Opciones")
#print("1 = Mayusculas")
#print("2 = Minusculas")
#print("3 = Primer letra maysucula")
#print("------------------------------")
#numero = int(input("Ingrese un numero mencionado: "))

#if numero == 1:
#    print(nombre.upper())
#elif numero == 2:
#    print(nombre.lower())
#elif numero == 3:
#    print(nombre.capitalize())
#else:
#    print("Opcion invalida.")

#--------------------------------------------------#
#ACTIVIDAD 9
#magnitud = int(input("Ingrese la magnitud del terremoto: "))

#if magnitud < 3:
#    print("Muy leve")
#elif magnitud >= 3 and magnitud < 4:
#    print("Leve")
#elif magnitud >= 4 and magnitud < 5:
#    print("Moderado")
#elif magnitud >= 5 and magnitud < 6:
#    print("Fuerte")
#elif magnitud >= 6 and magnitud < 7:
#    print("Muy fuerte")
#elif magnitud > 7:
#    print("Extremo")

#--------------------------------------------------#
#ACTIVIDAD 10
#hemisferio = input("Ingrese en qué hemisferio se encuentra (N/S): ").strip().upper()
#mes = int(input("Ingrese en qué mes del año se encuentra (1-12): "))
#dia = int(input("Ingrese el día en el que se encuentra (1-31): "))

#fecha = (mes, dia)

#if (fecha >= (12, 21) or fecha <= (3, 20)):
#    estacion = "invierno" if hemisferio == "N" else "verano"
#elif (fecha >= (3, 21) and fecha <= (6, 20)):
#    estacion = "primavera" if hemisferio == "N" else "otoño"
#elif (fecha >= (6, 21) and fecha <= (9, 20)):
#    estacion = "verano" if hemisferio == "N" else "invierno"
#else:  # del 21 de septiembre al 20 de diciembre
#    estacion = "otoño" if hemisferio == "N" else "primavera"

#print(f"La estación actual es: {estacion}")
