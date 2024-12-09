from utils import *

tablero = crear_tablero(10)

# La función input() permite obtener texto escrito por teclado.
coordenada_1 = input("¿cuál es tu coordenada 1?: ") 
coordenada_2 = input("introduce la coordenada 2: ")
tablero[int(coordenada_1)][int(coordenada_2)] = "X"

imprimir_tablero(tablero)

# iniciar en la terminal:
# os moveis hasta la carpeta donde tenéis el main con cd
# escribis en la terminal python main.py y pulsais enter