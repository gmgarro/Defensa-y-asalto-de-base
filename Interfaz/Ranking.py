from tkinter import *
from Clases.Jugador import Jugador

class Ranking:
    def __init__(self, root, volver_callback):
        self.root = root
        self.volver_callback = volver_callback

        self.canvas = Canvas(
            root,
            width=1200,
            height=600,
            bg="black",
            highlightthickness=0
        )
        self.canvas.pack()

        self.mostrar()

    def limpiar(self):
        self.canvas.delete("all")

    def destruir(self):
        self.canvas.destroy()

    def crear_boton(self, texto, x, y, accion):
        btn = Button(
            self.root,
            text=texto,
            command=accion,
            font=("Arial", 14, "bold"),
            bg="#111111",
            fg="white",
            activebackground="#001F63",
            activeforeground="white",
            bd=0,
            relief="flat",
            width=20,
            height=2
        )

        self.canvas.create_window(x, y, window=btn)

    def mostrar(self):
        self.limpiar()

        self.canvas.create_text(
            600, 80,
            text="RANKING DE VICTORIAS",
            fill="#3A7BFF",
            font=("Impact", 32)
        )

        # ── DEFENSORES ──
        self.canvas.create_text(
            300, 150,
            text="Defensores",
            fill="white",
            font=("Arial", 18, "bold")
        )

        top_def = Jugador.top_victorias_defensor()

        if not top_def:
            self.canvas.create_text(
                300, 250,
                text="No hay jugadores",
                fill="gray",
                font=("Arial", 14)
            )
        else:
            y = 200
            for i, (nombre, victorias) in enumerate(top_def, start=1):
                self.canvas.create_text(
                    300, y,
                    text=f"{i}. {nombre} - {victorias}",
                    fill="white",
                    font=("Arial", 14)
                )
                y += 30

        # ── ATACANTES ──
        self.canvas.create_text(
            900, 150,
            text="Atacantes",
            fill="white",
            font=("Arial", 18, "bold")
        )

        top_ata = Jugador.top_victorias_atacante()

        if not top_ata:
            self.canvas.create_text(
                900, 250,
                text="No hay jugadores",
                fill="gray",
                font=("Arial", 14)
            )
        else:
            y = 200
            for i, (nombre, victorias) in enumerate(top_ata, start=1):
                self.canvas.create_text(
                    900, y,
                    text=f"{i}. {nombre} - {victorias}",
                    fill="white",
                    font=("Arial", 14)
                )
                y += 30

        # ── BOTÓN VOLVER ──
        self.crear_boton("Volver", 600, 500, self.volver)
    
    def volver(self):
        self.destruir()
        self.volver_callback()