from Torre import Torre

class TorreBasica(Torre):
    def __init__(self):
        super().__init__(
            nombre="Torre Básica",
            costo=50,
            vida=80,
            dano=15,
            alcance=2,
            turnos_habilidad=3
        )
        
        self.disparo_doble = False

    def activar_habilidad(self, mapa):
        self.disparo_doble = True

    def atacar(self, Torre):
        super().atacar(Torre)

        if self.disparo_doble:
            super().atacar(Torre)
            self.disparo_doble = False