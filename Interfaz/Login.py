from tkinter import *
from Clases.Jugador import Jugador
from tkinter import messagebox


class Login:
    def __init__(self, root, callback_listo):
        self.root = root
        self.callback_listo = callback_listo

        self.faccion_defensor = StringVar(value="Medieval")
        self.faccion_atacante = StringVar(value="Futurista")

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

        self.mostrar_login()

    # ─────────────────────────────
    # CONTROL GENERAL
    # ─────────────────────────────

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

    # ─────────────────────────────
    # UI HELPERS
    # ─────────────────────────────

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

        btn.bind("<Enter>", lambda e: btn.config(bg="#001F63"))
        btn.bind("<Leave>", lambda e: btn.config(bg="#111111"))

        return btn

    def crear_selector_faccion(self, x, y, variable):
        opciones = ["Medieval", "Futurista", "Naturaleza"]

        selector = OptionMenu(
            self.root,
            variable,
            *opciones
        )

        selector.config(
            bg="#001F63",
            fg="white",
            activebackground="#3A7BFF",
            activeforeground="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            bd=0,
            width=15,
            highlightthickness=0,
            cursor="hand2"
        )

        menu = selector["menu"]
        menu.config(
            bg="#111111",
            fg="white",
            activebackground="#001F63",
            activeforeground="white",
            font=("Arial", 11),
            relief="flat",
            bd=0
        )

        self.canvas.create_window(x, y, window=selector)
        return selector

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

    # ─────────────────────────────
    # VALIDACIONES
    # ─────────────────────────────

    def facciones_validas(self):
        return self.faccion_defensor.get() != self.faccion_atacante.get()

    def usuarios_son_distintos(self, nombre, rol):
        if rol == "defensor" and self.jugador_atacante:
            return nombre != self.jugador_atacante.nombre
        if rol == "atacante" and self.jugador_defensor:
            return nombre != self.jugador_defensor.nombre
        return True

    def verificar_ambos_listos(self):
        if not self.jugador_defensor or not self.jugador_atacante:
            return

        if not self.facciones_validas():
            self.canvas.itemconfig(
                self.estado_defensor,
                text="No pueden usar la misma facción",
                fill="#FF4444"
            )
            self.canvas.itemconfig(
                self.estado_atacante,
                text="No pueden usar la misma facción",
                fill="#FF4444"
            )
            return

        self.callback_listo(
            self.jugador_defensor,
            self.jugador_atacante,
            self.faccion_defensor.get(),
            self.faccion_atacante.get()
        )

    # ─────────────────────────────
    # DEFENSOR
    # ─────────────────────────────

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

    # ─────────────────────────────
    # ATACANTE
    # ─────────────────────────────

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

    # ─────────────────────────────
    # PANTALLA LOGIN
    # ─────────────────────────────

    def mostrar_login(self):
        self.ajustar(1200, 600)
        self.limpiar()

        # ── DEFENSOR ──
        self.canvas.create_rectangle(50, 50, 575, 520, fill="#111111", outline="#001F63", width=3)
        self.canvas.create_text(312, 100, text="DEFENSOR", fill="#3A7BFF", font=("Impact", 28))

        self.canvas.create_text(132, 160, text="Usuario", fill="white", anchor="w")
        entry_user_def = self.crear_entry(320, 160)

        self.canvas.create_text(132, 220, text="Contraseña", fill="white", anchor="w")
        entry_pass_def = self.crear_entry(320, 220, es_password=True)

        self.crear_selector_faccion(320, 280, self.faccion_defensor)

        btn_def = self.crear_boton(
            "Confirmar",
            lambda: self.confirmar_defensor(entry_user_def, entry_pass_def)
        )
        self.canvas.create_window(312, 330, window=btn_def)

        self.estado_defensor = self.canvas.create_text(
            312, 380, text="", fill="white", font=("Arial", 10, "bold")
        )

        self.widgets_defensor = [entry_user_def, entry_pass_def]

        # ── ATACANTE ──
        self.canvas.create_rectangle(625, 50, 1150, 520, fill="#111111", outline="#001F63", width=3)
        self.canvas.create_text(887, 100, text="ATACANTE", fill="#3A7BFF", font=("Impact", 28))

        self.canvas.create_text(707, 160, text="Usuario", fill="white", anchor="w")
        entry_user_atk = self.crear_entry(895, 160)

        self.canvas.create_text(707, 220, text="Contraseña", fill="white", anchor="w")
        entry_pass_atk = self.crear_entry(895, 220, es_password=True)

        self.crear_selector_faccion(895, 280, self.faccion_atacante)

        btn_atk = self.crear_boton(
            "Confirmar",
            lambda: self.confirmar_atacante(entry_user_atk, entry_pass_atk)
        )
        self.canvas.create_window(887, 330, window=btn_atk)

        self.estado_atacante = self.canvas.create_text(
            887, 380, text="", fill="white", font=("Arial", 10, "bold")
        )

        self.widgets_atacante = [entry_user_atk, entry_pass_atk]