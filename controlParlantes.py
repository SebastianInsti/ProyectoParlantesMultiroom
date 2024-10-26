import requests

class Parlante:
    def __init__(self, ip):
        """
        Inicializa un objeto Parlante.
        
        :param ip: Dirección IP del parlante.
        """
        self.ip = ip
        self.volumen = 50  # Volumen por defecto al iniciar, puede ser configurable

    def set_volumen(self, nivel):
        """
        Configura el volumen del parlante.
        
        :param nivel: Nivel de volumen (0-100).
        """
        self.volumen = max(0, min(100, nivel))  # Asegura que el volumen esté entre 0 y 100
        try:
            # Ejemplo de solicitud HTTP para ajustar el volumen del parlante
            response = requests.post(f"http://{self.ip}/api/volume", json={"level": self.volumen})
            response.raise_for_status()
            print(f"Volumen de {self.ip} ajustado a {self.volumen}.")
        except requests.RequestException as e:
            print(f"Error al ajustar el volumen en {self.ip}: {e}")

    def subir_volumen(self, incremento=10):
        """
        Sube el volumen del parlante en una cantidad específica.
        
        :param incremento: Cantidad de volumen a subir (por defecto 10).
        """
        self.set_volumen(self.volumen + incremento)

    def bajar_volumen(self, decremento=10):
        """
        Baja el volumen del parlante en una cantidad específica.
        
        :param decremento: Cantidad de volumen a bajar (por defecto 10).
        """
        self.set_volumen(self.volumen - decremento)

    def apagar(self):
        """
        Apaga el parlante (si tiene soporte para esta funcionalidad).
        """
        try:
            response = requests.post(f"http://{self.ip}/api/power", json={"state": "off"})
            response.raise_for_status()
            print(f"Parlante en {self.ip} apagado.")
        except requests.RequestException as e:
            print(f"Error al apagar el parlante en {self.ip}: {e}")

    def encender(self):
        """
        Enciende el parlante (si tiene soporte para esta funcionalidad).
        """
        try:
            response = requests.post(f"http://{self.ip}/api/power", json={"state": "on"})
            response.raise_for_status()
            print(f"Parlante en {self.ip} encendido.")
        except requests.RequestException as e:
            print(f"Error al encender el parlante en {self.ip}: {e}")
