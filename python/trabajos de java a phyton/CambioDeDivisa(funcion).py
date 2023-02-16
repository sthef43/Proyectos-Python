def cambio_libras():
    libras = 0.86*euro
    print("El cambio de 1 euro a libras es:", libras)
    
def cambio_dolar():
    dolar =  1.28611 * euro
    print("El cambio de 1 euro a dolar es:", dolar)
    
def cambio_yenes():
    yenes = 129.852 * euro
    print("El cambio de 1 euro a yenes es:", yenes)
    
euro = int(input("ingrese la cantidad de euros:"))
cambio_libras()
cambio_dolar()
cambio_yenes()