from Clases.Torre import Torre

class TorrePesada(Torre):

    #e: ninguna
    #s: objeto TorrePesada inicializado
    # Crea una torre pesada con sus estadísticas y habilidad especial
    def __init__(self):
        super().__init__(
            nombre="Torre Pesada",
            costo=120,
            vida=200,
            dano=35,
            alcance=2,
            turnos_habilidad=4
        )

    #e: mapa
    #s: ninguna
    # Aplica daño a todas las unidades que se encuentran dentro de su alcance
    def activar_habilidad(self, mapa):

        unidades = mapa.unidades_en_rango(
            self.fila,
            self.columna,
            self.alcance
        )

        for unidad in unidades:
            unidad.recibir_dano(20)