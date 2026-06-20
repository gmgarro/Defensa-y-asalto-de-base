from Clases.Unidad import Unidad

class UnidadRapida(Unidad):

    #e: ninguna
    #s: objeto UnidadRapida inicializado
    # Crea una unidad rápida con sus estadísticas y habilidad especial
    def __init__(self):
        super().__init__(
            nombre="Unidad Rápida",
            costo=80,
            vida=70,
            dano=15,
            velocidad=3,
            habilidad="Aumento Velocidad",
            duracion_habilidad=2,
            posicion=(0, 0)   # 🔥 IMPORTANTE
        )

        self.velocidad_base = 3
        self.aumento_velocidad = False

    # ─────────────────────────────

    #e: ninguna
    #s: ninguna
    # Activa la habilidad y aumenta temporalmente la velocidad
    def activar_habilidad(self):
        if not self.aumento_velocidad:
            super().activar_habilidad()
            self.velocidad = self.velocidad_base + 2
            self.aumento_velocidad = True

    # ─────────────────────────────

    #e: objetivo a atacar
    #s: ninguna
    # Aplica daño al objetivo
    def atacar(self, objetivo):
        objetivo.recibir_dano(self.dano)

    # ─────────────────────────────

    #e: ninguna
    #s: ninguna
    # Actualiza la habilidad y restaura la velocidad original cuando termina
    def actualizar_habilidad(self):
        super().actualizar_habilidad()

        if not self.habilidad_activa and self.aumento_velocidad:
            self.velocidad = self.velocidad_base
            self.aumento_velocidad = False