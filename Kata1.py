from datetime import date

lightyears = 3.26156

print("Este es un programa que te indica la fecha actual y hace conversiones de parsecs a años luz")
print("Antes de continuar, introduzca su nombre completo por favor")

name = input("Nombre: ")

parsec = input ("Introducta la cantidad de parsecs a convertir: ")
convertToLY = float(parsec) * lightyears 

print("Hola " + str(name) + ", la fecha actual es: " + str(date.today()))
print(str(parsec) + " parsercs son equivalentes a " + str(convertToLY) + " años luz.")