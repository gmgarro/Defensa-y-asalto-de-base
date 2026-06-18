import json
import os


class Jugador:

    ARCHIVO_DATOS = "../Datos/usuarios.json"

    def __init__(self, nombre, password):
        self.nombre = nombre
        self.password = password
        self.victorias_defensor = 0
        self.victorias_atacante = 0

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "password": self.password,
            "victorias_defensor": self.victorias_defensor,
            "victorias_atacante": self.victorias_atacante
        }

    @classmethod
    def cargar_todos(cls):
        if not os.path.exists(cls.ARCHIVO_DATOS):
            return {}

        try:
            with open(cls.ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except:
            return {}

    @classmethod
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
    def iniciar_sesion(cls, nombre, password):

        usuarios = cls.cargar_todos()

        if nombre in usuarios and usuarios[nombre]["password"] == password:

            jugador = cls(nombre, password)

            jugador.victorias_defensor = usuarios[nombre]["victorias_defensor"]
            jugador.victorias_atacante = usuarios[nombre]["victorias_atacante"]

            return jugador

        return None

    def guardar_victorias(self):

        usuarios = self.cargar_todos()

        if self.nombre in usuarios:

            usuarios[self.nombre]["victorias_defensor"] = self.victorias_defensor
            usuarios[self.nombre]["victorias_atacante"] = self.victorias_atacante

            with open(self.ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
                json.dump(usuarios, archivo, indent=4)

    def sumar_victoria_defensor(self):
        self.victorias_defensor += 1
        self.guardar_victorias()

    def sumar_victoria_atacante(self):
        self.victorias_atacante += 1
        self.guardar_victorias()