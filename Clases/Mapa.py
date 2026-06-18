from Base import Base


class Mapa:

    def __init__(self):

        self.filas = 10
        self.columnas = 10

        self.matriz = [
            [None for _ in range(self.columnas)]
            for _ in range(self.filas)
        ]

        self.base = Base()

        self.base_fila = 5
        self.base_columna = 5

        self.matriz[self.base_fila][self.base_columna] = self.base

    def obtener_casilla(self, fila, columna):

        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            return self.matriz[fila][columna]

        return None

    def colocar_objeto(self, fila, columna, objeto):

        if not (0 <= fila < self.filas and 0 <= columna < self.columnas):
            return False

        if self.matriz[fila][columna] is not None:
            return False

        self.matriz[fila][columna] = objeto

        if hasattr(objeto, "fila"):
            objeto.fila = fila

        if hasattr(objeto, "columna"):
            objeto.columna = columna

        return True

    def eliminar_objeto(self, fila, columna):

        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            self.matriz[fila][columna] = None

    def mostrar(self):

        for fila in self.matriz:

            for casilla in fila:

                if casilla is None:
                    print(".", end=" ")

                elif isinstance(casilla, Base):
                    print("B", end=" ")

                else:
                    print("X", end=" ")

            print()