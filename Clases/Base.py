class Base:

    #e: ninguna
    #s: objeto Base inicializado
    # Inicializa la base con vida y sin posición asignada
    def __init__(self):
        self.vida = 500
        self.fila = None
        self.columna = None

    #e: daño recibido
    #s: ninguna
    # Reduce la vida de la base según el daño recibido
    def recibir_dano(self, dano):
        self.vida -= dano

        if self.vida < 0:
            self.vida = 0

    #e: ninguna
    #s: valor booleano
    # Indica si la base fue destruida
    def esta_destruida(self):
        return self.vida <= 0