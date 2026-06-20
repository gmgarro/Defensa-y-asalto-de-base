import json
import os


class Jugador:

    # Ruta donde se encuentra el archivo de usuarios
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ARCHIVO_DATOS = os.path.join(BASE_DIR, "..", "Datos", "usuarios.json")

    #e: nombre del jugador, contraseña
    #s: objeto Jugador inicializado
    # Crea un nuevo jugador con sus datos y victorias en cero
    def __init__(self, nombre, password):
        self.nombre = nombre
        self.password = password
        self.victorias_defensor = 0
        self.victorias_atacante = 0

    #e: ninguna
    #s: diccionario con los datos del jugador
    # Convierte los atributos del jugador en un diccionario
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "password": self.password,
            "victorias_defensor": self.victorias_defensor,
            "victorias_atacante": self.victorias_atacante
        }

    @classmethod
    #e: ninguna
    #s: diccionario con todos los usuarios registrados
    # Carga la información almacenada en el archivo JSON
    def cargar_todos(cls):
        if not os.path.exists(cls.ARCHIVO_DATOS):
            return {}

        try:
            with open(cls.ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except:
            return {}

    @classmethod
    #e: nombre de usuario, contraseña
    #s: True si se registra, False si ya existe
    # Registra un nuevo usuario en el archivo
    def registrar_en_archivo(cls, nombre, password):

        usuarios = cls.cargar_todos()

        if nombre in usuarios:
            return False

        jugador = cls(nombre, password)

        usuarios[nombre] = jugador.to_dict()

        with open(cls.ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
            json.dump(usuarios, archivo, indent=4)

        return True

    @classmethod
    #e: nombre de usuario, contraseña
    #s: objeto Jugador o None
    # Verifica las credenciales e inicia sesión
    def iniciar_sesion(cls, nombre, password):

        usuarios = cls.cargar_todos()

        if nombre in usuarios and usuarios[nombre]["password"] == password:

            jugador = cls(nombre, password)

            jugador.victorias_defensor = usuarios[nombre]["victorias_defensor"]
            jugador.victorias_atacante = usuarios[nombre]["victorias_atacante"]

            return jugador

        return None

    #e: ninguna
    #s: ninguna
    # Guarda las victorias actuales del jugador en el archivo
    def guardar_victorias(self):

        usuarios = self.cargar_todos()

        if self.nombre in usuarios:

            usuarios[self.nombre]["victorias_defensor"] = self.victorias_defensor
            usuarios[self.nombre]["victorias_atacante"] = self.victorias_atacante

            with open(self.ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
                json.dump(usuarios, archivo, indent=4)

    #e: ninguna
    #s: ninguna
    # Suma una victoria como defensor y la guarda
    def sumar_victoria_defensor(self):
        self.victorias_defensor += 1
        self.guardar_victorias()

    #e: ninguna
    #s: ninguna
    # Suma una victoria como atacante y la guarda
    def sumar_victoria_atacante(self):
        self.victorias_atacante += 1
        self.guardar_victorias()

    @classmethod
    #e: nombre del campo a consultar
    #s: lista con los cinco mejores jugadores
    # Obtiene el top 5 de jugadores según el campo indicado
    def top_victorias(cls, campo):
        usuarios = cls.cargar_todos()

        jugadores = [
            (nombre, datos.get(campo, 0))
            for nombre, datos in usuarios.items()
            if datos.get(campo, 0) > 0
        ]

        jugadores.sort(key=lambda x: x[1], reverse=True)
        return jugadores[:5]

    @classmethod
    #e: ninguna
    #s: lista con los cinco mejores defensores
    # Obtiene el top de victorias como defensor
    def top_victorias_defensor(cls):
        return cls.top_victorias("victorias_defensor")

    @classmethod
    #e: ninguna
    #s: lista con los cinco mejores atacantes
    # Obtiene el top de victorias como atacante
    def top_victorias_atacante(cls):
        return cls.top_victorias("victorias_atacante")