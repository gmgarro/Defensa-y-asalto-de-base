from Clases.Torre import Torre

class TorrePesada(Torre):

    def __init__(self):
        super().__init__(
            nombre="Torre Pesada",
            costo=120,
            vida=200,
            dano=35,
            alcance=2,
            turnos_habilidad=4
        )

    def activar_habilidad(self, mapa):

        unidades = mapa.unidades_en_rango(
            self.fila,
            self.columna,
            self.alcance
        )

        for unidad in unidades:
            unidad.recibir_dano(20)