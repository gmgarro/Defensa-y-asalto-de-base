from Torre import Torre

class TorreMagica(Torre):

    def __init__(self):
        super().__init__(
            nombre="Torre Mágica",
            costo=90,
            vida=60,
            dano=10,
            alcance=3,
            turnos_habilidad=3
        )

    def activar_habilidad(self, mapa):

        unidad = mapa.unidad_mas_cercana(
            self.fila,
            self.columna,
            self.alcance
        )

        if unidad:
            unidad.turnos_congelada = 2
