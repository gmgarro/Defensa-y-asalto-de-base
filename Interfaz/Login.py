from tkinter import *

from Clases.Jugador import Jugador


class Login:
    def __init__(self, root, callback_listo):
        self.root = root
        self.callback_listo = callback_listo

        self.canvas = Canvas(
            root,
            width=1200,
            height=600,
            bg="black",
            highlightthickness=0
        )
        self.canvas.pack()

        self.jugador_defensor = None
        self.jugador_atacante = None

        self.widgets_defensor = []
        self.widgets_atacante = []

        self.estado_defensor = None
        self.estado_atacante = None
        self.pendiente_registro = None
        
        self.mostrar_login()

    # ── IMPORTANTE PARA MAIN ──
    def destruir(self):
        for w in self.widgets_defensor + self.widgets_atacante:
            w.destroy()
        self.canvas.destroy()

    def limpiar(self):
        self.canvas.delete("all")
        for w in self.widgets_defensor + self.widgets_atacante:
            w.destroy()
        self.widgets_defensor = []
        self.widgets_atacante = []

    def ajustar(self, ancho, alto):
        self.root.geometry(f"{ancho}x{alto}")
        self.canvas.config(width=ancho, height=alto)

    def crear_boton(self, texto, accion, ancho=18):
        btn = Button(
            self.root,
            text=texto,
            command=accion,
            font=("Arial", 12, "bold"),
            bg="#111111",
            fg="white",
            activebackground="#001F63",
            activeforeground="white",
            bd=0,
            relief="flat",
            width=ancho,
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

    def crear_entry(self, x, y, es_password=False):
        entry = Entry(
            self.root,
            font=("Arial", 12),
            bg="#1C1C1C",
            fg="white",
            insertbackground="white",
            relief="flat",
            width=22,
            justify="center",
            show="*" if es_password else ""
        )
        self.canvas.create_window(x, y, window=entry)
        return entry

    # ── LÓGICA COMPARTIDA ──
    def usuarios_son_distintos(self, nombre, rol):
        if rol == "defensor" and self.jugador_atacante:
            return nombre != self.jugador_atacante.nombre
        if rol == "atacante" and self.jugador_defensor:
            return nombre != self.jugador_defensor.nombre
        return True

    def verificar_ambos_listos(self):
        if self.jugador_defensor and self.jugador_atacante:
            self.callback_listo(self.jugador_defensor, self.jugador_atacante)

    # ── ACCIONES DEFENSOR ──
    def confirmar_defensor(self, entry_usuario, entry_password):
        nombre = entry_usuario.get().strip()
        password = entry_password.get().strip()

        if not nombre or not password:
            self.canvas.itemconfig(
                self.estado_defensor,
                text="Completá usuario y contraseña",
                fill="#FF4444"
            )
            return

        if not self.usuarios_son_distintos(nombre, "defensor"):
            self.canvas.itemconfig(
                self.estado_defensor,
                text="Ya elegido por el atacante",
                fill="#FF4444"
            )
            return

        jugador = Jugador.iniciar_sesion(nombre, password)

        if not jugador:
            usuarios = Jugador.cargar_todos()

            if nombre not in usuarios:
                from tkinter import messagebox

                respuesta = messagebox.askyesno(
                    "Usuario no encontrado",
                    f"El usuario '{nombre}' no existe.\n¿Deseas registrarlo?"
                )

                if respuesta:
                    Jugador.registrar_en_archivo(nombre, password)
                    jugador = Jugador.iniciar_sesion(nombre, password)
                else:
                    self.canvas.itemconfig(
                        self.estado_defensor,
                        text="Registro cancelado",
                        fill="#FF4444"
                    )
                    return
            else:
                self.canvas.itemconfig(
                    self.estado_defensor,
                    text="Contraseña incorrecta",
                    fill="#FF4444"
                )
                return

        self.jugador_defensor = jugador
        self.canvas.itemconfig(
            self.estado_defensor,
            text=f"Listo: {nombre}",
            fill="#3A7BFF"
        )
        self.verificar_ambos_listos()

    # ── ACCIONES ATACANTE ──
    def confirmar_atacante(self, entry_usuario, entry_password):
        nombre = entry_usuario.get().strip()
        password = entry_password.get().strip()

        if not nombre or not password:
            self.canvas.itemconfig(
                self.estado_atacante,
                text="Completá usuario y contraseña",
                fill="#FF4444"
            )
            return

        if not self.usuarios_son_distintos(nombre, "atacante"):
            self.canvas.itemconfig(
                self.estado_atacante,
                text="Ya elegido por el defensor",
                fill="#FF4444"
            )
            return

        jugador = Jugador.iniciar_sesion(nombre, password)

        if not jugador:
            usuarios = Jugador.cargar_todos()

            if nombre not in usuarios:
                from tkinter import messagebox

                respuesta = messagebox.askyesno(
                    "Usuario no encontrado",
                    f"El usuario '{nombre}' no existe.\n¿Deseas registrarlo?"
                )

                if respuesta:
                    Jugador.registrar_en_archivo(nombre, password)
                    jugador = Jugador.iniciar_sesion(nombre, password)
                else:
                    self.canvas.itemconfig(
                        self.estado_atacante,
                        text="Registro cancelado",
                        fill="#FF4444"
                    )
                    return
            else:
                self.canvas.itemconfig(
                    self.estado_atacante,
                    text="Contraseña incorrecta",
                    fill="#FF4444"
                )
                return

        self.jugador_atacante = jugador
        self.canvas.itemconfig(
            self.estado_atacante,
            text=f"Listo: {nombre}",
            fill="#3A7BFF"
        )
        self.verificar_ambos_listos()

    # ── PANTALLA ──
    def mostrar_login(self):
        self.ajustar(1200, 600)
        self.limpiar()

        # ── Panel izquierdo: DEFENSOR ──
        self.canvas.create_rectangle(
            50, 50, 575, 520,
            fill="#111111",
            outline="#001F63",
            width=3
        )
        self.canvas.create_text(
            312, 100,
            text="DEFENSOR",
            fill="#3A7BFF",
            font=("Impact", 28)
        )

        self.canvas.create_text(312 - 180, 160, text="Usuario", fill="white", font=("Arial", 11), anchor="w")
        entry_user_def = self.crear_entry(320, 160)

        self.canvas.create_text(312 - 180, 220, text="Contraseña", fill="white", font=("Arial", 11), anchor="w")
        entry_pass_def = self.crear_entry(320, 220, es_password=True)

        btn_def = self.crear_boton(
            "Confirmar",
            lambda: self.confirmar_defensor(entry_user_def, entry_pass_def)
        )
        self.canvas.create_window(312, 300, window=btn_def)

        self.estado_defensor = self.canvas.create_text(
            312, 360, text="", fill="white", font=("Arial", 10, "bold")
        )

        self.widgets_defensor = [entry_user_def, entry_pass_def]

        # ── Panel derecho: ATACANTE ──
        self.canvas.create_rectangle(
            625, 50, 1150, 520,
            fill="#111111",
            outline="#001F63",
            width=3
        )
        self.canvas.create_text(
            887, 100,
            text="ATACANTE",
            fill="#3A7BFF",
            font=("Impact", 28)
        )

        self.canvas.create_text(887 - 180, 160, text="Usuario", fill="white", font=("Arial", 11), anchor="w")
        entry_user_atk = self.crear_entry(895, 160)

        self.canvas.create_text(887 - 180, 220, text="Contraseña", fill="white", font=("Arial", 11), anchor="w")
        entry_pass_atk = self.crear_entry(895, 220, es_password=True)

        btn_atk = self.crear_boton(
            "Confirmar",
            lambda: self.confirmar_atacante(entry_user_atk, entry_pass_atk)
        )
        self.canvas.create_window(887, 300, window=btn_atk)

        self.estado_atacante = self.canvas.create_text(
            887, 360, text="", fill="white", font=("Arial", 10, "bold")
        )

        self.widgets_atacante = [entry_user_atk, entry_pass_atk]