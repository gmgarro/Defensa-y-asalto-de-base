from Clases.Unidad import Unidad

class Soldado(Unidad):

    #e: ninguna
    #s: objeto Soldado inicializado
    # Crea un soldado con sus estadísticas y habilidad especial
    def __init__(self):
        super().__init__(
            nombre="Soldado",
            costo=50,
            vida=100,
            dano=20,
            velocidad=2,
            habilidad="Disparo doble",
            duracion_habilidad=1,
            posicion=(0, 0) 
        )

        self.disparo_doble = False

    # ─────────────────────────────

    #e: ninguna
    #s: ninguna
    # Activa la habilidad de disparo doble
    def activar_habilidad(self):
        super().activar_habilidad()
        self.disparo_doble = True

    # ─────────────────────────────

    #e: unidad objetivo
    #s: ninguna
    # Ataca a una unidad y realiza un segundo ataque si la habilidad está activa
    def atacar(self, unidad):
        super().atacar(unidad)

        if self.disparo_doble:
            super().atacar(unidad)
            self.disparo_doble = False
            self.habilidad_activa = False
            self.turnos_restantes_habilidad = 0