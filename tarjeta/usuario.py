"""Esta función únicamente nos despliega un diccionario en donde se encuentran datos para
el estado de cuenta de una tarjeta de crédito"""


def creaTarjeta():
    """Esta función solicita una serie de datos para generar cálculos y para ordenarlos 
    en un reporte de pagos"""
    nombre = input("Nombre de la tarjeta: ")
    tasaAnual = float(input("Tasa de interés anual de la tarjeta (%): "))
    deuda = float(input("Escribe el monto de la deuda actual de la tarjeta: "))
    pago = float(input("Escribe el monto del pago a realizar: "))
        
    #Si el pago es mayor a la deuda, solicitamos que intente de nuevo el procedimiento
    if pago > deuda:
        print("No es posible realizar un pago mayor a la deuda, intente de nuevo.")
        return
    else:
        pass

    cargos = float(input("Escribe el monto total de los nuevos cargos: "))
    #Generamos un diccionario con los datos recabados
    return {"Nombre de Tarjeta":nombre,
    "Tasa Anual":tasaAnual,
    "Deuda Actual":deuda,
    "Monto del Pago":pago,
    "Nuevos cargos del mes":cargos}