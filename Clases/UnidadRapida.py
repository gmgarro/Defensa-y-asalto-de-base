from Unidad import Unidad

class UnidadRapida(Unidad):
    def __init__(self):
        super().__init__(
            nombre="Unidad Rápida",
            costo=80,
            vida=70,
            dano=15,
            velocidad=3,
            habilidad="Aumento Velocidad",
            turnos_habilidad=2
        )
        
        self.aumento_velocidad = False
        
        
    def activar_habilidad(self):
        self.velocidad += 2
    
    def atacar(self, objetivo):
        objetivo.recibir_dano(self.dano)
    