from tkinter import Tk

from Interfaz.Menu import Menu
from Interfaz.Ranking import Ranking
from Interfaz.Login import Login


class Main:
    def __init__(self, root):
        self.root = root
        self.pantalla_actual = None

        self.j1 = None
        self.j2 = None

        self.mostrar_menu()

    # ── LIMPIAR PANTALLA ACTUAL ──
    def limpiar(self):
        if self.pantalla_actual:
            self.pantalla_actual.destruir()
            self.pantalla_actual = None

    # ── MENÚ ──
    def mostrar_menu(self):
        self.limpiar()
        self.pantalla_actual = Menu(
            self.root,
            self.mostrar_ranking,
            self.mostrar_login_partida
        )

    # ── LOGIN DE PARTIDA (2 JUGADORES) ──
    def mostrar_login_partida(self):
        self.limpiar()
        self.pantalla_actual = Login(
            self.root,
            self.iniciar_partida
        )

    def iniciar_partida(self, j1, j2):
        self.j1 = j1
        self.j2 = j2
        self.mostrar_juego()

    # ── RANKING ──
    def mostrar_ranking(self):
        self.limpiar()
        self.pantalla_actual = Ranking(
            self.root,
            self.mostrar_menu
        )

    # ── JUEGO ──
    def mostrar_juego(self):
        self.limpiar()

        print("PARTIDA INICIADA")
        print("Jugador 1:", self.j1.nombre)
        print("Jugador 2:", self.j2.nombre)


# ── EJECUCIÓN ──
root = Tk()
root.title("Defensa y Asalto de Base")
root.geometry("1200x600")

app = Main(root)

root.mainloop()