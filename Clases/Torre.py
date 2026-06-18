class Torre:
    def __init__(self, nombre, costo, vida, dano, alcance, turnos_habilidad):
        self.nombre = nombre
        self.costo = costo
        self.vida = vida
        self.dano = dano
        self.alcance = alcance
        self.turnos_habilidad = turnos_habilidad 
        self.turnos_transcurridos = 0
        self.fila = None
        self.columna = None

    def recibir_dano(self, cantidad):
        self.vida -= cantidad

    def esta_viva(self):
        return self.vida > 0

    def activar_habilidad(self, mapa):
        raise NotImplementedError("Cada torre debe implementar su habilidad")

    def intentar_habilidad(self, mapa):
        self.turnos_transcurridos += 1
        if self.turnos_transcurridos >= self.turnos_habilidad:
            self.activar_habilidad(mapa)
            self.turnos_transcurridos = 0

    def atacar(self, unidad):
        unidad.recibir_dano(self.dano)
        
    def __str__(self):
        return f"{self.nombre} | Vida: {self.vida} | Daño: {self.dano} | Alcance: {self.alcance}"
    
