import os
os.system("cls")

#ACTIVIDADES
#------------------------------------------------
#EJERCICIO 1

#def imprimir_hola_mundo():
#    print("Hola Mundo!")

#if __name__ == "__main__":
#    imprimir_hola_mundo()
#------------------------------------------------

#EJERCICIO 2

#def saludar_usuario(nombre):
#    print(f"Hola {nombre}")

#if __name__ == "__main__":
#    saludar_usuario("Alejo")

#------------------------------------------------

#EJERCICIO 3

#nombre = input("Ingrese su nombre: ")
#apellido = input("Ingrese su apellido: ")
#edad = int(input("Ingrese su edad: "))
#residencia = input("Ingrese su residencia: ")

#def informacion_personal(nombre, apellido, edad, residencia):
#    print(f"Hola soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#if __name__ == "__main__":
#    informacion_personal(nombre, apellido, edad, residencia)

#------------------------------------------------

#EJERCICIO 4

#radio = int(input("Ingrese el radio del circulo: "))
#area_circulo = 3.14 * radio ** 2
#diametro = 2 * radio
#perimetro_circulo = diametro * 3.14

#def calcular_perimetro_circulo (radio):
#    print(f"El perimetro del circulo es: {perimetro_circulo}")

#def calcular_area_circulo(radio):
#   print(f"El area del circulo es: {area_circulo}")

#if __name__ == "__main__":
#    calcular_area_circulo(radio)

#if __name__ == "__main__":
#    calcular_perimetro_circulo(radio)

#------------------------------------------------

#EJERCICIO 5

#def segundos_a_horas(segundos):
#    horas = segundos / 3600
#    print(f"La cantidad de horas segun los segundos que pusiste es de: {horas:.2f}hs.")

#if __name__ == "__main__":
#    segundos = int(input("Ingrese una cantidad de segundos: "))
#   segundos_a_horas(segundos)

#------------------------------------------------

#EJERCICIO 6

#numero = int(input("Ingrese un numero: "))

#def tabla_multiplicar(numero):
#    for i in range (1,11):
#        resultado = numero * i
#        print(f"{numero} x {i} = {resultado}")

#tabla_multiplicar(numero)

#------------------------------------------------

#EJERCICIO 7

#a = int(input("Ingrese el primer numero: "))
#b = int(input("Ingrese el segundo numero: "))

#def operaciones_basicas(a, b):
#    suma = a + b
#    resta = a - b
#    multiplicacion = a * b
#    division = a / b
#    return (suma, resta, multiplicacion, division)
#resultados = operaciones_basicas(a,b)
#print(f"El resultado de la suma es: {resultados[0]}")
#print(f"El resultado de la resta es: {resultados[1]}")
#print(f"El resultado de la multiplicacion es: {resultados[2]}")
#print(f"El resultado de la division es: {resultados[3]}")

#------------------------------------------------

#EJERCICIO 8

#peso = float(input("Ingrese su peso corporal: "))
#altura = float(input("Ingrese su altura: "))

#def calcular_imc (peso, altura):
#    imc = peso / altura ** 2
#    print(f"El indice de masa corporal es de: {imc:.2f}")

#calcular_imc(peso, altura)

#------------------------------------------------

#EJERCICIO 9

#celsius = float(input("Ingrese una temperatura en Celsius: "))

#def celsius_a_fahrenheit(celsius):
#    fahrenheit = (celsius * 9/5) + 32
#    print(f"La temperatura de Celsius a Fahrenheit es de: {fahrenheit}°F")

#celsius_a_fahrenheit(celsius)

#------------------------------------------------

#EJERCICIO 10

#a = float(input("Ingrese el primer numero: "))
#b = float(input("Ingrese el segundo numero: "))
#c = float(input("Ingrese el tercer numero: "))


#def calcular_promedio (a, b, c):
#    return (a + b + c) / 3

#promedio_final = calcular_promedio (a, b, c)
#print(f"El promedio de los numeros ingresados es de: {promedio_final}")

