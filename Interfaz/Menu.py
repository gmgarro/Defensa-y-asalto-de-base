import os
from tkinter import *

class Menu:
    def __init__(self, root, callback_ranking, callback_juego):
        self.root = root
        self.callback_ranking = callback_ranking
        self.callback_juego = callback_juego

        self.canvas = Canvas(
            root,
            width=1200,
            height=600,
            bg="black",
            highlightthickness=0
        )
        self.canvas.pack()

        self.mostrar_menu()

    # ── IMPORTANTE PARA MAIN ──
    def destruir(self):
        self.canvas.destroy()

    def limpiar(self):
        self.canvas.delete("all")

    def ajustar(self, ancho, alto):
        self.root.geometry(f"{ancho}x{alto}")
        self.canvas.config(width=ancho, height=alto)

    def crear_boton(self, texto, accion):
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
            height=2,
            cursor="hand2"
        )

        def entrar(e):
            btn.config(bg="#001F63")

        def salir(e):
            btn.config(bg="#111111")

        btn.bind("<Enter>", entrar)
        btn.bind("<Leave>", salir)

        return btn

    # ── ACCIONES ──
    def iniciar_juego(self):
        self.callback_juego()

    def mostrar_estadisticas(self):
        self.callback_ranking()

    def salir(self):
        self.root.destroy()

    # ── PANTALLA ──
    def mostrar_menu(self):
        self.ajustar(1200, 600)
        self.limpiar()

        ruta = os.path.join(
            os.path.dirname(__file__),
            "..",
            "Recursos",
            "Imagenes",
            "main_background.png"
        )

        try:
            fondo = PhotoImage(file=ruta)
            self.canvas.fondo = fondo
            self.canvas.create_image(0, 0, image=fondo, anchor="nw")
        except:
            self.canvas.config(bg="black")

        centro_x = 600

        self.canvas.create_rectangle(
            275, 50, 900, 450,
            fill="#111111",
            outline="#001F63",
            width=3
        )

        self.canvas.create_text(
            centro_x, 130,
            text="DEFENSA Y ASALTO DE BASE",
            fill="#3A7BFF",
            font=("Impact", 36)
        )

        btn_jugar = self.crear_boton("Jugar", self.iniciar_juego)
        btn_stats = self.crear_boton("Ranking", self.mostrar_estadisticas)
        btn_salir = self.crear_boton("Salir", self.salir)

        self.canvas.create_window(centro_x, 250, window=btn_jugar)
        self.canvas.create_window(centro_x, 320, window=btn_stats)
        self.canvas.create_window(centro_x, 390, window=btn_salir)