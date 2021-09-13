

import os
os.system("clear")

nombre = input("Nombre del dueño de la tarjeta: ")
tasaAnual = float(input("Tasa de interés anual de la tarjeta (%): "))
deuda = float(input("Escribe el monto de la deuda actual de la tarjeta: "))
pago = float(input("Escribe el monto del pago a realizar: "))
cargos = float(input("Escribe el monto total de los nuevos cargos: "))

def creaTarjeta():
	