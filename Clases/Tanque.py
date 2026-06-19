from Unidad import Unidad

class Tanque(Unidad):
    def __init__(self):
        super().__init__(
            nombre="Tanque",
            costo=120,
            vida=250,
            dano=35,
            velocidad=1,
            habilidad="Escudo Temporal",
            duracion_habilidad=4
        )

        self.escudo_temporal = False

    def activar_habilidad(self):
        super().activar_habilidad()
        self.escudo_temporal = True

    def actualizar_habilidad(self):
        super().actualizar_habilidad()

        if not self.habilidad_activa:
            self.escudo_temporal = False

    def recibir_dano(self, cantidad):
        if self.escudo_temporal:
            cantidad = cantidad // 2

        self.vida -= cantidad

        if self.vida < 0:
            self.vida = 0

    def atacar(self, objetivo):
        objetivo.recibir_dano(self.dano)