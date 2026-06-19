from tkinter import Tk
from Interfaz.Menu import Menu
from Interfaz.Ranking import Ranking
# from Interfaz.Juego import Juego  (lo agregaremos después)


class Main:
    def __init__(self, root):
        self.root = root
        self.pantalla_actual = None
        self.mostrar_menu()

    def limpiar(self):
        if self.pantalla_actual is not None:
            self.pantalla_actual.destruir()
            self.pantalla_actual = None

    # ── MENU ──
    def mostrar_menu(self):
        self.limpiar()
        self.pantalla_actual = Menu(
            self.root,
            self.mostrar_ranking,
            self.mostrar_juego  # 👈 FALTA AGREGAR ESTO
        )

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
        print("Aquí irá la pantalla de juego")  # luego lo reemplazamos


# ── EJECUCIÓN ──
root = Tk()
root.title("Defensa y Asalto de Base")
root.geometry("1200x600")

app = Main(root)

root.mainloop()