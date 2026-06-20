class Unidad:
       #e: nombre, costo, vida, daño, velocidad, habilidad, duración de habilidad y posición
    #s: objeto Unidad inicializado
    # Crea una unidad con sus estadísticas, habilidad y posición inicial
    def __init__(
        self,
        nombre,
        costo,
        vida,
        dano,
        velocidad,
        habilidad,
        duracion_habilidad,
        posicion=(0, 0)
    ):

        self.nombre = nombre
        self.costo = costo
        self.vida = vida
        self.dano = dano
        self.velocidad = velocidad

        self.habilidad = habilidad
        self.duracion_habilidad = duracion_habilidad

        self.turnos_restantes_habilidad = 0
        self.turnos_congelada = 0
        self.habilidad_activa = False

        # ─────────────────────────────
        # COORDENADAS (ÚNICA FUENTE REAL)
        # ─────────────────────────────
        self.fila = posicion[0]
        self.columna = posicion[1]

    # ─────────────────────────────
    # COMBATE
    # ─────────────────────────────

    #e: objetivo a atacar
    #s: ninguna
    # Aplica daño al objetivo
    def atacar(self, objetivo):
        objetivo.recibir_dano(self.dano)

    #e: cantidad de daño
    #s: ninguna
    # Reduce la vida de la unidad
    def recibir_dano(self, cantidad):
        self.vida = max(0, self.vida - cantidad)

    # ─────────────────────────────
    # MOVIMIENTO (SIN ROMPER MAPA)
    # ─────────────────────────────

    #e: nueva posición
    #s: ninguna
    # Mueve la unidad a una nueva posición si no está congelada
    def mover(self, nueva_posicion):
        if self.turnos_congelada > 0:
            self.turnos_congelada -= 1
            return

        self.fila = nueva_posicion[0]
        self.columna = nueva_posicion[1]

    # ─────────────────────────────
    # ESTADO
    # ─────────────────────────────

    #e: ninguna
    #s: valor booleano
    # Indica si la unidad sigue con vida
    def esta_viva(self):
        return self.vida > 0

    # ─────────────────────────────
    # HABILIDAD
    # ─────────────────────────────

    #e: ninguna
    #s: ninguna
    # Activa la habilidad especial de la unidad
    def activar_habilidad(self):
        self.habilidad_activa = True
        self.turnos_restantes_habilidad = self.duracion_habilidad

    #e: ninguna
    #s: ninguna
    # Actualiza la duración restante de la habilidad
    def actualizar_habilidad(self):
        if self.habilidad_activa:
            self.turnos_restantes_habilidad -= 1

            if self.turnos_restantes_habilidad <= 0:
                self.habilidad_activa = False
                self.turnos_restantes_habilidad = 0

    # ─────────────────────────────

    #e: ninguna
    #s: cadena de texto
    # Devuelve una representación en texto de la unidad
    def __str__(self):
        return f"{self.nombre} | Vida: {self.vida} | Daño: {self.dano}"