from Clases.Torre import Torre

class TorreMagica(Torre):

    #e: ninguna
    #s: objeto TorreMagica inicializado
    # Crea una torre mágica con sus estadísticas y habilidad especial
    def __init__(self):
        super().__init__(
            nombre="Torre Mágica",
            costo=90,
            vida=60,
            dano=10,
            alcance=3,
            turnos_habilidad=3
        )

    #e: mapa
    #s: ninguna
    # Congela a la unidad enemiga más cercana dentro de su alcance
    def activar_habilidad(self, mapa):

        unidad = mapa.unidad_mas_cercana(
            self.fila,
            self.columna,
            self.alcance
        )

        if unidad:
            unidad.turnos_congelada = 2
