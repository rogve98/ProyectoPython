"""Este programa brinda un resumen de la información y calcula el monto del prózimo pago mensual """

import os
os.system("clear")


#Solicitamos valores de entrada
nombre = input("Nombre del dueño de la tarjeta: ")
tasaAnual = float(input("Tasa de interés anual de la tarjeta (%): "))
deuda = float(input("Escribe el monto de la deuda actual de la tarjeta: "))
pago = float(input("Escribe el monto del pago a realizar: "))
cargos = float(input("Escribe el monto total de los nuevos cargos: "))
    
#Generamos un condicional que nos diga si podemos proceder o no con la operación    
if pago > deuda:
    print("No es posible realizar un pago mayot a la deuda, intente de nuevo.")
else:   
    interesMensual = tasaAnual/12
    deudaRecalculada = (deuda - pago)*(1+interesMensual)
    nuevaDeuda = deudaRecalculada + cargos
    despuesdePago = deuda-pago
    print("")
    print("Resumen de tarjeta:")  
    print("-"*40)
    print(f"Tarjeta a nombre de:    {nombre}")
    print(f"Tasa de interés anual:  {tasaAnual:.2f}%")
    print("-"*40)
    print(f"Deuda actual:           {deuda:.2f}")
    print(f"Monto del pago:         {pago:.2f}")
    print("-"*40)
    print(f"Deuda después del pago: {despuesdePago:.2f}")
    print(f"Intereses del mes       {interesMensual:.2f}")
    print("-"*40)
    print(f"Deuda recalculada       {deudaRecalculada:.2f}")
    print(f"Nuevos cargos del mes:  {cargos:.2f}")
    print("-"*40)
    print(f"Nueva deuda del mes:    {nuevaDeuda:.2f}")

     
