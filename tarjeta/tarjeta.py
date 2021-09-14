"""Las siguientes funciones realizan cálculos para recalcular deudas, genera una lista con la 
información de un diccionario con datos, y por último nos imprime dicha información en forma de
reporte de tarjeta. """


def capturaNuevaTarjeta(diccionario):
    """Esta función hará una serie de cálculos para notar el interés mensual,
     y deudas recalculada con base en los datos solicitados """
    interesMensual = diccionario["Tasa Anual"]/12
    deudaRecalculada = (diccionario["Deuda Actual"] - diccionario["Monto del Pago"])*(1+interesMensual)
    nuevaDeuda = deudaRecalculada + diccionario["Nuevos cargos del mes"]
    despuesdePago = diccionario["Deuda Actual"]-diccionario["Monto del Pago"]
    
    #Agregamos nuevos datos al diccionario que se creó en la función anterior 
    #para poder ocuparlo en la impresión del reporte
    diccionario["Deuda después del pago"] = despuesdePago
    diccionario["Interés Mensual"] = interesMensual
    diccionario["Deuda Recalculada"] = deudaRecalculada
    diccionario["Nueva deuda del mes"] = nuevaDeuda
    return diccionario

def generaReporte(diccionario):
    """Esta función generará una lista para ordenar los datos del 
    diccionario con la información disponible"""
    
    #Vamos a crear un par de listas con la información de las llaves y valores de nuestro diccionario, 
    #para luego crear y ordenar dichos datos para después imprimirlos 
    leyendas = list(diccionario.keys())
    datos = list(diccionario.values())
    reporte = [[leyendas[0], datos[0]],
            [leyendas[1],datos[1]],
            [leyendas[2],datos[2]],
            [leyendas[3],datos[3]],
            [leyendas[5],datos[5]],
            [leyendas[6],datos[6]],
            [leyendas[7],datos[7]],
            [leyendas[4],datos[4]],
            [leyendas[8],datos[8]],
            ]
    return reporte
            
def imprimeReporte(reporte):
    """Esta función imprimirá el reporte de la tarjeta conforme a los cálculos y datos solicitados. """
    print()
    print("-"*40)
    print("-"*11 + "Resumen de tarjeta:" + "-"*10)
    print("-"*40)
    print(f"{reporte[0][0]}:    {reporte[0][1]}")
    print(f"{reporte[1][0]}:    {reporte[1][1]:.2f}%")
    print("-"*40)
    print(f"{reporte[2][0]}:    {reporte[2][1]:.2f}")
    print(f"{reporte[3][0]}:    {reporte[3][1]:.2f}")
    print("-"*40)
    print(f"{reporte[4][0]}:    {reporte[4][1]:.2f}")
    print(f"{reporte[5][0]}:    {reporte[5][1]:.2f}")
    print("-"*40)
    print(f"{reporte[6][0]}:    {reporte[6][1]:.2f}")
    print(f"{reporte[7][0]}:    {reporte[7][1]:.2f}")
    print("-"*40)
    print(f"{reporte[8][0]}:    {reporte[8][1]:.2f}") 