import cv2
from controlParlantes import Parlante  # Asumiendo que existe un módulo para controlar parlantes

# Cargar la configuración
configuracion = cargar_configuracion()

# Inicializar las cámaras según la configuración
camaras = {}
for camara in configuracion["camaras"]:
    camaras[camara["nombre"]] = cv2.VideoCapture(camara["indice"])  # Usa índice local o IP de la cámara

# Inicializar los parlantes según la configuración
parlantes = {}
for parlante in configuracion["parlantes"]:
    parlantes[parlante["nombre"]] = Parlante(parlante["ip"])
    parlantes[parlante["nombre"]].set_volumen(parlante["volumen_inicial"])
