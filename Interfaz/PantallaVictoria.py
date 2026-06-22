from tkinter import *


class PantallaVictoria:

    COLOR_FONDO = "#0D0D0D"
    COLOR_PANEL = "#111111"
    COLOR_ACENTO = "#3A7BFF"
    COLOR_TEXTO = "white"
    COLOR_ORO = "#FFD700"

    #e: ventana principal, ganador, victorias del defensor y victorias del atacante
    #s: objeto PantallaVictoria inicializado
    # Muestra el resultado final de la partida y permite volver al menú
    def __init__(self, root, callback_menu, ganador, victorias_defensor, victorias_atacante):
        self.root = root
        self.callback_menu = callback_menu

        self.ganador = ganador
        self.victorias_defensor = victorias_defensor
        self.victorias_atacante = victorias_atacante

        self.frame_principal = Frame(root, bg=self.COLOR_FONDO)
        self.frame_principal.pack(fill="both", expand=True)

        self.mostrar_pantalla()

    # ── IMPORTANTE PARA MAIN ──
    def destruir(self):
        self.frame_principal.destroy()

    # =====================================
    # VOLVER AL MENU
    # =====================================

    def volver_menu(self):
        self.callback_menu()

    # =====================================
    # PANTALLA
    # =====================================

    def mostrar_pantalla(self):

        Label(
            self.frame_principal,
            text="¡PARTIDA FINALIZADA!",
            font=("Impact", 36),
            bg=self.COLOR_FONDO,
            fg=self.COLOR_ACENTO
        ).pack(pady=(80, 20))

        Label(
            self.frame_principal,
            text=f"Ganador: {self.ganador.nombre}",
            font=("Arial", 18, "bold"),
            bg=self.COLOR_FONDO,
            fg=self.COLOR_ORO
        ).pack(pady=10)

        Label(
            self.frame_principal,
            text=(
                f"Marcador final: "
                f"{self.victorias_defensor} - "
                f"{self.victorias_atacante}"
            ),
            font=("Arial", 14),
            bg=self.COLOR_FONDO,
            fg=self.COLOR_TEXTO
        ).pack(pady=10)

        # =====================
        # BOTON VOLVER AL MENU
        # =====================

        btn_menu = Button(
            self.frame_principal,
            text="Volver al Menú",
            command=self.volver_menu,
            font=("Arial", 14, "bold"),
            bg="#111111",
            fg="white",
            activebackground=self.COLOR_ACENTO,
            activeforeground="white",
            bd=0,
            relief="flat",
            width=20,
            height=2,
            cursor="hand2"
        )

        btn_menu.pack(pady=40)

        btn_menu.bind("<Enter>", lambda e: btn_menu.config(bg=self.COLOR_ACENTO))
        btn_menu.bind("<Leave>", lambda e: btn_menu.config(bg="#111111"))