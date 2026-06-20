from Clases.Base import Base


class Mapa:

    #e: tamaño del mapa
    #s: objeto Mapa inicializado
    # Crea el mapa con una base en el centro y los colores de las facciones
    def __init__(self, size=15):

        self.size = size

        # Matriz principal
        self.grid = [
            [None for _ in range(size)]
            for _ in range(size)
        ]

        # Base central
        self.base = Base()

        self.base.fila = size // 2
        self.base.columna = size // 2

        self.grid[self.base.fila][self.base.columna] = self.base

        # Colores para la interfaz
        self.facciones = {
            "Medieval": {
                "base": "#8B0000",
                "torre": "#A0522D",
                "unidad": "#CD853F",
                "muro": "#696969"
            },

            "Futurista": {
                "base": "#00BFFF",
                "torre": "#1E90FF",
                "unidad": "#00FFFF",
                "muro": "#708090"
            },

            "Naturaleza": {
                "base": "#228B22",
                "torre": "#6B8E23",
                "unidad": "#7CFC00",
                "muro": "#2E8B57"
            }
        }

    # =====================================================
    # VALIDACIONES
    # =====================================================

    #e: fila, columna
    #s: valor booleano
    # Verifica si una posición está dentro de los límites del mapa
    def en_rango(self, fila, columna):
        return (
            0 <= fila < self.size and
            0 <= columna < self.size
        )

    #e: fila, columna
    #s: valor booleano
    # Indica si una celda está libre
    def celda_libre(self, fila, columna):

        if not self.en_rango(fila, columna):
            return False

        return self.grid[fila][columna] is None

    # =====================================================
    # COLOCAR OBJETOS
    # =====================================================

    #e: fila, columna, objeto
    #s: valor booleano
    # Coloca un objeto en una posición del mapa
    def colocar(self, fila, columna, objeto):

        if not self.en_rango(fila, columna):
            return False

        if not self.celda_libre(fila, columna):
            return False

        self.grid[fila][columna] = objeto

        objeto.fila = fila
        objeto.columna = columna

        return True

    # =====================================================
    # ELIMINAR OBJETO
    # =====================================================

    #e: fila, columna
    #s: valor booleano
    # Elimina un objeto del mapa si no corresponde a la base
    def eliminar(self, fila, columna):

        if not self.en_rango(fila, columna):
            return False

        if self.grid[fila][columna] is self.base:
            return False

        self.grid[fila][columna] = None

        return True

    # =====================================================
    # MOVIMIENTO DE UNIDADES
    # =====================================================

    #e: unidad, nueva fila, nueva columna
    #s: valor booleano
    # Mueve una unidad a una nueva posición del mapa
    def mover_unidad(self, unidad, nueva_fila, nueva_columna):

        if not self.en_rango(nueva_fila, nueva_columna):
            return False

        fila_actual = unidad.fila
        columna_actual = unidad.columna

        # Si el destino es la celda actual de la propia unidad, no hay nada que mover
        if (fila_actual, columna_actual) == (nueva_fila, nueva_columna):
            return True

        # La celda destino debe estar libre o ser la celda que la unidad ya ocupaba
        if self.grid[nueva_fila][nueva_columna] is not None:
            return False

        # Solo se limpia la celda de origen si efectivamente la ocupaba esta unidad,
        # evitando borrar referencias de otro objeto que haya quedado ahi por error
        if self.en_rango(fila_actual, columna_actual):
            if self.grid[fila_actual][columna_actual] is unidad:
                self.grid[fila_actual][columna_actual] = None

        self.grid[nueva_fila][nueva_columna] = unidad

        unidad.mover((nueva_fila, nueva_columna))

        return True

    # =====================================================
    # DAÑO A LA BASE
    # =====================================================

    #e: cantidad de daño
    #s: ninguna
    # Aplica daño a la base del mapa
    def danar_base(self, dano):
        self.base.recibir_dano(dano)

    # =====================================================
    # CONSULTAS
    # =====================================================

    #e: fila, columna
    #s: objeto o None
    # Obtiene el objeto que se encuentra en una posición
    def obtener_objeto(self, fila, columna):

        if not self.en_rango(fila, columna):
            return None

        return self.grid[fila][columna]

    # =====================================================
    # TORRES
    # =====================================================

    #e: fila, columna, alcance
    #s: unidad o None
    # Busca la unidad viva más cercana dentro del alcance indicado
    def unidad_mas_cercana(self, fila, columna, alcance):

        mejor = None
        mejor_distancia = 999999

        for i in range(self.size):
            for j in range(self.size):

                obj = self.grid[i][j]

                if obj is None:
                    continue

                # Solo unidades vivas
                if not hasattr(obj, "velocidad"):
                    continue

                if hasattr(obj, "esta_viva") and not obj.esta_viva():
                    continue

                distancia = max(
                    abs(fila - i),
                    abs(columna - j)
                )

                if distancia <= alcance:

                    if distancia < mejor_distancia:
                        mejor = obj
                        mejor_distancia = distancia

        return mejor

    #e: fila, columna, alcance
    #s: lista de unidades
    # Obtiene todas las unidades vivas dentro del alcance indicado
    def unidades_en_rango(self, fila, columna, alcance):

        unidades = []

        for i in range(self.size):
            for j in range(self.size):

                obj = self.grid[i][j]

                if obj is None:
                    continue

                if not hasattr(obj, "velocidad"):
                    continue

                if hasattr(obj, "esta_viva") and not obj.esta_viva():
                    continue

                distancia = max(
                    abs(fila - i),
                    abs(columna - j)
                )

                if distancia <= alcance:
                    unidades.append(obj)

        return unidades

    # =====================================================
    # REINICIAR RONDA
    # =====================================================

    #e: ninguna
    #s: ninguna
    # Reinicia el mapa y vuelve a crear la base en el centro
    def reiniciar(self):

        self.grid = [
            [None for _ in range(self.size)]
            for _ in range(self.size)
        ]

        self.base = Base()

        self.base.fila = self.size // 2
        self.base.columna = self.size // 2

        self.grid[self.base.fila][self.base.columna] = self.base