import os
import random
os.system("cls")

#EJERCICIO 1
#for i in range (0,101):

#    print (i)

#--------------------------------------------------#

#EJERCICIO 2
#numero = input("Ingrese un numero entero: ")

#contador_digitos = len(numero)

#print(f"El numero tiene {contador_digitos} digitos")

#--------------------------------------------------#

#EJERCICIO 3
#numero1 = int(input("Ingrese el primer numero solicitado: "))
#numero2 = int(input("Ingrese el segundo numero solicitado: "))

#inicio = min (numero1,numero2 + 1)
#fin = max (numero1,numero2)

#suma = 0

#for i in range (inicio, fin):
#    suma = i + 1

#print(f"La suma de los números entre {numero1} y {numero2}, excluyéndolos, es: {suma}") 

#--------------------------------------------------#
#EJERCICIO 4
#suma_total = 0

#print("Ingrese numeros 1 por 1. Ingrese el numero 0 para finalizar")

#while True:
#     numero = int(input("Ingrese un número: "))

#     if numero == 0:
#          break
     
#     suma_total += numero

#print(f"La suma total de los números ingresados es: {suma_total}")

#--------------------------------------------------#
#EJERCICIO 5
#numero_random = random.randint(0,9)
#intentos = 0

#while True:
#    intento = int(input("Adivine el numero: "))
#    intentos += 1

#    if intento == numero_random:
#        print(f"¡Correcto! Adivinaste el número en {intentos} intento(s).")
#        break
#    else:
#        print("Incorrecto ")

#--------------------------------------------------#
#EJERCICIO 6
#num1 = 0
#num2 = 100

#for i in range(max(num1, num2), min(num1, num2) - 1, -1):
#    if i % 2 == 0:
#        print(i)

#--------------------------------------------------#
#EJERCICIO 7
#num1 = 0
#num2 = int(input("Ingrese un numero entero: "))

#for i in range (max(num1, num2),min(num1, num2) - 1, -1):
#        print(i)
   
#--------------------------------------------------#
#EJERCICIO 8
#CANTIDAD_NUMEROS = 100

#pares = 0
#impares = 0
#positivos = 0
#negativos = 0

#print(f"Ingrese {CANTIDAD_NUMEROS} números enteros:")

#for i in range(CANTIDAD_NUMEROS):
#    numero = int(input(f"Número {i + 1}: "))
    
#    if numero % 2 == 0:
#        pares += 1
#    else:
#        impares += 1

#    if numero > 0:
#        positivos += 1
#    elif numero < 0:
#        negativos += 1
    
#print("\nResultados:")
#print(f"Pares: {pares}")
#print(f"Impares: {impares}")
#print(f"Positivos: {positivos}")
#print(f"Negativos: {negativos}")

#--------------------------------------------------#
#EJERCICIO 9
#CANTIDAD_NUMEROS = 10

#suma_numeros = 0

#print(f"Ingrese {CANTIDAD_NUMEROS} números enteros:")

#for i in range(CANTIDAD_NUMEROS):
#    numero = int(input(f"Número {i + 1}: "))
#    suma_numeros += numero
    
#media = suma_numeros/CANTIDAD_NUMEROS
#print(f"La media de los numeros ingresados es {media}:")

#--------------------------------------------------#
#EJERCICIO 10
#numero = int(input("Ingrese un numero: "))

#invertir = int(str(abs(numero))[::-1])

#if numero < 0: 
#    invertir *= -1

#print(f"El numero invertido seria {invertir}")
