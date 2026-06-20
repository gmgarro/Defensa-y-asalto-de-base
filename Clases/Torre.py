class Torre:

    #e: nombre, costo, vida, daño, alcance y turnos para la habilidad
    #s: objeto Torre inicializado
    # Crea una torre con sus estadísticas básicas
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

    #e: cantidad de daño
    #s: ninguna
    # Reduce la vida de la torre según el daño recibido
    def recibir_dano(self, cantidad):
        self.vida -= cantidad

        if self.vida < 0:
            self.vida = 0

    #e: ninguna
    #s: valor booleano
    # Indica si la torre sigue con vida
    def esta_viva(self):
        return self.vida > 0

    #e: mapa
    #s: ninguna
    # Método que debe ser implementado por cada tipo de torre
    def activar_habilidad(self, mapa):
        raise NotImplementedError("Cada torre debe implementar su habilidad")

    #e: mapa
    #s: ninguna
    # Controla cuándo debe activarse la habilidad especial de la torre
    def intentar_habilidad(self, mapa):
        self.turnos_transcurridos += 1
        if self.turnos_transcurridos >= self.turnos_habilidad:
            self.activar_habilidad(mapa)
            self.turnos_transcurridos = 0

    #e: unidad objetivo
    #s: ninguna
    # Aplica daño a una unidad
    def atacar(self, unidad):
        unidad.recibir_dano(self.dano)

    #e: ninguna
    #s: cadena de texto
    # Devuelve una representación en texto de la torre
    def __str__(self):
        return f"{self.nombre} | Vida: {self.vida} | Daño: {self.dano} | Alcance: {self.alcance}"