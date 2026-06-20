from tkinter import Tk

from Clases.Partida import Partida
from Interfaz.Menu import Menu
from Interfaz.Ranking import Ranking
from Interfaz.Login import Login
from Interfaz.Juego import Juego
from Clases.Mapa import Mapa


class Main:

    #e: ventana principal de tkinter
    #s: objeto Main inicializado
    # Crea la aplicación principal y muestra el menú inicial
    def __init__(self, root):
        self.root = root
        self.pantalla_actual = None

        self.j1 = None
        self.j2 = None

        self.mostrar_menu()

    # ── LIMPIAR PANTALLA ACTUAL ──

    #e: ninguna
    #s: ninguna
    # Elimina la pantalla actual antes de cargar una nueva
    def limpiar(self):
        if self.pantalla_actual:
            self.pantalla_actual.destruir()
            self.pantalla_actual = None

    # ── MENÚ ──

    #e: ninguna
    #s: ninguna
    # Muestra la pantalla principal del menú
    def mostrar_menu(self):
        self.limpiar()
        self.pantalla_actual = Menu(
            self.root,
            self.mostrar_ranking,
            self.mostrar_login_partida
        )

    # ── LOGIN DE PARTIDA (2 JUGADORES) ──

    #e: ninguna
    #s: ninguna
    # Muestra la pantalla de inicio de sesión para los jugadores
    def mostrar_login_partida(self):
        self.limpiar()
        self.pantalla_actual = Login(
            self.root,
            self.iniciar_partida
        )

    #e: jugador defensor, jugador atacante, facción defensora y facción atacante
    #s: ninguna
    # Crea una nueva partida con los datos seleccionados
    def iniciar_partida(self, j1, j2, faccion_defensor, faccion_atacante):
        self.j1 = j1
        self.j2 = j2
        self.faccion_defensor = faccion_defensor
        self.faccion_atacante = faccion_atacante

        self.mapa = Mapa()

        self.partida = Partida(
            self.j1,
            self.j2,
            self.faccion_defensor,
            self.faccion_atacante,
            self.mapa
        )

        self.mostrar_juego()

    # ── RANKING ──

    #e: ninguna
    #s: ninguna
    # Muestra la pantalla de ranking de jugadores
    def mostrar_ranking(self):
        self.limpiar()
        self.pantalla_actual = Ranking(
            self.root,
            self.mostrar_menu
        )

    # ── JUEGO ──

    #e: ninguna
    #s: ninguna
    # Muestra la interfaz principal del juego
    def mostrar_juego(self):
        self.limpiar()

        self.pantalla_actual = Juego(
            self.root,
            self.partida
        )

# ── EJECUCIÓN ──
root = Tk()
root.title("Defensa y Asalto de Base")
root.geometry("1200x600")

app = Main(root)

root.mainloop()