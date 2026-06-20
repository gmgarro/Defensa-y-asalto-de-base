from Clases.Unidad import Unidad

class Tanque(Unidad):

    #e: ninguna
    #s: objeto Tanque inicializado
    # Crea un tanque con sus estadísticas y habilidad especial
    def __init__(self):
        super().__init__(
            nombre="Tanque",
            costo=120,
            vida=250,
            dano=35,
            velocidad=1,
            habilidad="Escudo Temporal",
            duracion_habilidad=4,
            posicion=(0, 0)  
        )

        self.escudo_temporal = False

    # ─────────────────────────────

    #e: ninguna
    #s: ninguna
    # Activa la habilidad de escudo temporal
    def activar_habilidad(self):
        super().activar_habilidad()
        self.escudo_temporal = True

    # ─────────────────────────────

    #e: ninguna
    #s: ninguna
    # Actualiza el estado de la habilidad y desactiva el escudo cuando termina
    def actualizar_habilidad(self):
        super().actualizar_habilidad()

        # cuando termina la habilidad, se desactiva el escudo
        if not self.habilidad_activa:
            self.escudo_temporal = False

    # ─────────────────────────────

    #e: cantidad de daño
    #s: ninguna
    # Reduce la vida del tanque tomando en cuenta el escudo temporal
    def recibir_dano(self, cantidad):
        if self.escudo_temporal:
            cantidad = cantidad // 2

        self.vida -= cantidad

        if self.vida < 0:
            self.vida = 0

    # ─────────────────────────────

    #e: objetivo a atacar
    #s: ninguna
    # Aplica daño al objetivo
    def atacar(self, objetivo):
        objetivo.recibir_dano(self.dano)