from Clases.Torre import Torre

class TorreBasica(Torre):

    #e: ninguna
    #s: objeto TorreBasica inicializado
    # Crea una torre básica con sus estadísticas y habilidad especial
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

    #e: mapa
    #s: ninguna
    # Activa la habilidad de disparo doble
    def activar_habilidad(self, mapa):
        self.disparo_doble = True

    #e: unidad objetivo
    #s: ninguna
    # Ataca al objetivo y realiza un segundo ataque si la habilidad está activa
    def atacar(self, Torre):
        super().atacar(Torre)

        if self.disparo_doble:
            super().atacar(Torre)
            self.disparo_doble = False