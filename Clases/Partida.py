class Partida:
    def __init__(self):
        self.unidades_atacantes = []
        self.unidades_defensoras = []
        self.turno = 1
        self.base_vida = 500
        self.juego_activo = True

    def agregar_atacante(self, unidad):
        self.unidades_atacantes.append(unidad)

    def agregar_defensor(self, unidad):
        self.unidades_defensoras.append(unidad)

    def mover_atacantes(self):
        for unidad in self.unidades_atacantes:
            x, y = unidad.posicion
            nueva_pos = (x + unidad.velocidad, y)
            unidad.mover(nueva_pos)

    def combate(self):
        for atacante in self.unidades_atacantes:
            for defensor in self.unidades_defensoras:
                if atacante.posicion == defensor.posicion and atacante.esta_viva() and defensor.esta_viva():
                    atacante.atacar(defensor)

                    if defensor.esta_viva():
                        defensor.atacar(atacante)

    def daño_a_base(self):
        for unidad in self.unidades_atacantes:
            if unidad.esta_viva() and unidad.posicion == (10, 10):
                self.base_vida -= unidad.dano
                unidad.vida = 0

    def limpiar_muertos(self):
        self.unidades_atacantes = [u for u in self.unidades_atacantes if u.esta_viva()]
        self.unidades_defensoras = [u for u in self.unidades_defensoras if u.esta_viva()]

    def siguiente_turno(self):
        self.turno += 1

        for u in self.unidades_atacantes + self.unidades_defensoras:
            u.actualizar_habilidad()

        self.mover_atacantes()
        self.combate()
        self.daño_a_base()
        self.limpiar_muertos()

        if self.base_vida <= 0:
            self.juego_activo = False
            print("¡Ganaron los atacantes!")

        if len(self.unidades_atacantes) == 0:
            self.juego_activo = False
            print("¡Ganaron los defensores!")

    def estado(self):
        return {
            "turno": self.turno,
            "base_vida": self.base_vida,
            "atacantes": len(self.unidades_atacantes),
            "defensores": len(self.unidades_defensoras)
        }