from utils import ordenar_carpeta
from variables import ruta_carpeta, categorias

# categorias = {"Documentos": ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx'),
#               "Imagenes": ('.jpg', '.jpeg', '.png', '.svg', '.gif'),
#               "Softwares": ('.exe', '.py','.ipynb'),
#             #   "Data": ('.csv'),
#               "Otros": ()}
# ruta_carpeta = "./carpeta_prueba"
# ruta_carpeta = "D:/Bootcamps_DS/24_11_Bootcamp_DS/2411_dsft_thebridge/2-Data-Analysis/3-Sources/Archivos/Practica/carpeta_prueba"

ordenar_carpeta(ruta_carpeta, categorias)