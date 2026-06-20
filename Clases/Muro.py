class Muro:

    #e: ninguna
    #s: objeto Muro inicializado
    # Crea un muro con su costo, vida y posición inicial
    def __init__(self):
        self.costo = 50
        self.vida = 150
        
        self.fila = None
        self.columna = None

    #e: cantidad de daño
    #s: ninguna
    # Reduce la vida del muro según el daño recibido
    def recibir_dano(self, dano):
        self.vida -= dano

        if self.vida < 0:
            self.vida = 0

    #e: ninguna
    #s: valor booleano
    # Indica si el muro fue destruido
    def esta_destruido(self):
        return self.vida <= 0
