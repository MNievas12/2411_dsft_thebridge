from utils import Fichero
from variables import ruta_carpeta, categorias


for categoria in categorias:
    fichero = Fichero(categoria, categorias[categoria], ruta_carpeta)
    fichero.crear_carpeta()
    fichero.mover()