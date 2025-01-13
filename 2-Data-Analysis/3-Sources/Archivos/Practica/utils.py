import os
import shutil

# categorias = {"Documentos": ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx'),
#               "Imagenes": ('.jpg', '.jpeg', '.png', '.svg', '.gif'),
#               "Softwares": ('.exe', '.py','.ipynb'),
#             #   "Data": ('.csv'),
#               "Otros": ()}
# ruta_carpeta = "./carpeta_prueba"

def ordenar_carpeta(ruta_carpeta, categorias):
    for categoria in categorias.keys():
        os.makedirs(ruta_carpeta + "/" + categoria, exist_ok=True)
    
    for archivo in os.listdir(ruta_carpeta):
        ruta_archivo = ruta_carpeta + "/" + archivo
        if os.path.isdir(ruta_archivo):
            print("Carpeta:", archivo)
        else:
            print("Archivo:", archivo)
            if archivo.endswith(categorias['Documentos']):
                print("Mover archivo a Documentos")
                shutil.move(ruta_archivo, ruta_carpeta + "/Documentos")
            elif archivo.endswith(categorias['Imagenes']):
                print("Mover archivo a Imagenes")
                shutil.move(ruta_archivo, ruta_carpeta + "/Imagenes")
            elif archivo.endswith(categorias['Softwares']):
                print("Mover archivo a Softwares")
                shutil.move(ruta_archivo, ruta_carpeta + "/Softwares")
            else:
                print("Mover archivo a Otros")
                shutil.move(ruta_archivo, ruta_carpeta + "/Otros")
    
class Fichero:

    def __init__(self, categoria, extensiones, ruta):
        self.categoria = categoria
        self.extensiones = extensiones
        self.ruta = ruta
    
    def crear_carpeta(self):
        os.makedirs(self.ruta + "/" + self.categoria, exist_ok=True)

    def mover(self):
        for archivo in os.listdir(self.ruta):
            ruta_archivo = self.ruta + "/" + archivo
            if os.path.isdir(ruta_archivo):
                pass
            elif archivo.endswith(self.extensiones) or self.categoria == "Otros":
                shutil.move(ruta_archivo, self.ruta + "/" + self.categoria)
        