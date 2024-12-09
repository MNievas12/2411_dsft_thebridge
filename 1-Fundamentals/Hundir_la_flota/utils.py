def crear_tablero(tamano):
    """
    Funcion que crea el tablero. 

    Args: tamano - el tamaño del tablero

    returns -> una lista de tamano x tamano llena de "-" 

    """
    
    tablero = []

    for i in range(tamano):
        fila = []
        for j in range(tamano):
            fila.append("_")
        tablero.append(fila)
    
    return tablero

def imprimir_tablero(tablero):
    print("imprimimos el tablero")
    for i in range(len(tablero)):
        print(*tablero[1])