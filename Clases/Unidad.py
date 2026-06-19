class Unidad:
    def __init__(self, nombre, costo, vida, dano, velocidad, habilidad, duracion_habilidad, posicion=(0, 0)):
        self.nombre = nombre
        self.costo = costo
        self.vida = vida
        self.dano = dano
        self.velocidad = velocidad
        self.habilidad = habilidad
        self.duracion_habilidad = duracion_habilidad
        self.turnos_restantes_habilidad = 0
        self.posicion = posicion
        self.turnos_congelada = 0
        self.habilidad_activa = False

    def atacar(self, objetivo):
        objetivo.recibir_dano(self.dano)

    def recibir_dano(self, cantidad):
        self.vida -= cantidad

        if self.vida < 0:
            self.vida = 0

    def mover(self, nueva_posicion):
        if self.turnos_congelada > 0:
            self.turnos_congelada -= 1
            return

        self.posicion = nueva_posicion

    def esta_viva(self):
        return self.vida > 0

    def activar_habilidad(self):
        self.habilidad_activa = True
        self.turnos_restantes_habilidad = self.duracion_habilidad

    def actualizar_habilidad(self):
        if self.habilidad_activa:
            self.turnos_restantes_habilidad -= 1

            if self.turnos_restantes_habilidad <= 0:
                self.habilidad_activa = False
                self.turnos_restantes_habilidad = 0

    def __str__(self):
        return f"{self.nombre} | Vida: {self.vida} | Daño: {self.dano}"