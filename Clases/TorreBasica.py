from Torre import Torre

class TorreBasica(Torre):
    def __init__(self):
        super().__init__(
            nombre="Torre Básica",
            costo=50,
            vida=80,
            daño=15,
            alcance=2,
            turnos_habilidad=3
        )

    def activar_habilidad(self, mapa):
        # Disparo doble: retorna True para indicar que este turno ataca dos veces
        self.disparo_doble = True

    def atacar(self, unidad):
        unidad.recibir_daño(self.daño)
        if hasattr(self, 'disparo_doble') and self.disparo_doble:
            unidad.recibir_daño(self.daño)
            self.disparo_doble = False