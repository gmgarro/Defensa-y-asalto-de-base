from tkinter import *
from tkinter import messagebox

import os
from PIL import Image, ImageTk

from Clases.Base import Base
from Clases.Muro import Muro

from Clases.TorreBasica import TorreBasica
from Clases.TorrePesada import TorrePesada
from Clases.TorreMagica import TorreMagica

from Clases.Soldado import Soldado
from Clases.Tanque import Tanque
from Clases.UnidadRapida import UnidadRapida


class Juego:

    COLOR_FONDO = "#0D0D0D"
    COLOR_PANEL = "#111111"
    COLOR_ACENTO = "#3A7BFF"
    COLOR_CELDA = "#1C1C1C"
    COLOR_BORDE_CELDA = "#2A2A2A"
    COLOR_TEXTO = "white"
    COLOR_ORO = "#FFD700"
    COLOR_ALERTA = "#FF4444"

    CARPETA_IMAGENES = os.path.join("Recursos", "Imagenes")

    def __init__(self, root, partida):

        self.root = root
        self.partida = partida

        self.tam_celda = 40

        self.opcion = StringVar(value="Muro")

        # Cache de imagenes ya cargadas y redimensionadas, para no leer
        # el archivo de disco ni reescalar en cada ciclo del loop.
        # Clave: "tipo_faccion" en minuscula (ej: "torrebasica_medieval")
        # Valor: objeto ImageTk.PhotoImage listo para usar, o None si
        # la imagen no existe o no se pudo cargar (se usara color de relleno).
        self.cache_imagenes = {}

        # Guarda los ids de rectangulo y de objeto que ya se dibujaron en
        # cada celda, para no tener que borrar y recrear todo el canvas
        # en cada ciclo del loop (eso es lo que causaba el parpadeo).
        self.celdas_fondo = {}
        self.celdas_objeto = {}

        self.frame_principal = Frame(root, bg=self.COLOR_FONDO)
        self.frame_principal.pack(fill="both", expand=True)

        # ============================
        # TABLERO
        # ============================

        ancho_canvas = self.partida.mapa.size * self.tam_celda
        alto_canvas = self.partida.mapa.size * self.tam_celda

        self.canvas = Canvas(
            self.frame_principal,
            width=ancho_canvas,
            height=alto_canvas,
            bg=self.COLOR_FONDO,
            highlightthickness=0
        )

        self.canvas.pack(side=LEFT)

        self.canvas.bind(
            "<Button-1>",
            self.click_mapa
        )

        self.dibujar_fondo_mapa()

        # ============================
        # PANEL
        # ============================

        self.panel = Frame(
            self.frame_principal,
            width=300,
            bg=self.COLOR_PANEL
        )

        self.panel.pack(
            side=RIGHT,
            fill="y"
        )

        self.crear_panel()

        self.loop()

    # =====================================
    # PASAR FASE
    # =====================================

    def pasar_fase(self):

        if self.partida.fase == "ATAQUE" and self.partida.oro_atacante >= 50:

            continuar = messagebox.askyesno(
                "Oro disponible",
                "Aun tienes oro suficiente para colocar mas unidades.\n"
                "¿Deseas pasar a la fase de combate de todas formas?"
            )

            if not continuar:
                return

        self.partida.pasar_fase()

    # =====================================
    # DESTRUIR
    # =====================================

    def destruir(self):
        self.frame_principal.destroy()

    # =====================================
    # PANEL
    # =====================================

    def crear_panel(self):

        Label(
            self.panel,
            text="DEFENSA Y ASALTO DE BASE",
            font=("Impact", 16),
            bg=self.COLOR_PANEL,
            fg=self.COLOR_ACENTO
        ).pack(pady=(15, 10))

        # ── Marcador de ronda y fase ──
        marco_estado = Frame(self.panel, bg=self.COLOR_PANEL)
        marco_estado.pack(fill="x", padx=15, pady=5)

        self.lbl_ronda = Label(
            marco_estado, font=("Arial", 12, "bold"),
            bg=self.COLOR_PANEL, fg=self.COLOR_TEXTO
        )
        self.lbl_ronda.pack(anchor="w")

        self.lbl_fase = Label(
            marco_estado, font=("Arial", 11),
            bg=self.COLOR_PANEL, fg=self.COLOR_ACENTO
        )
        self.lbl_fase.pack(anchor="w")

        # ── Marcador de victorias ──
        self.lbl_score = Label(
            self.panel, font=("Arial", 12, "bold"),
            bg=self.COLOR_PANEL, fg=self.COLOR_TEXTO
        )
        self.lbl_score.pack(pady=10)

        # ── Vida de la base ──
        self.lbl_base = Label(
            self.panel, font=("Arial", 11, "bold"),
            bg=self.COLOR_PANEL, fg=self.COLOR_TEXTO
        )
        self.lbl_base.pack(pady=(5, 10))

        # ── Oro de cada jugador ──
        marco_oro = Frame(self.panel, bg=self.COLOR_PANEL)
        marco_oro.pack(fill="x", padx=15, pady=5)

        self.lbl_oro_def = Label(
            marco_oro, font=("Arial", 10, "bold"),
            bg=self.COLOR_PANEL, fg=self.COLOR_ORO
        )
        self.lbl_oro_def.pack(anchor="w")

        self.lbl_oro_atk = Label(
            marco_oro, font=("Arial", 10, "bold"),
            bg=self.COLOR_PANEL, fg=self.COLOR_ORO
        )
        self.lbl_oro_atk.pack(anchor="w")

        # ── Selector de objetos a colocar ──
        Label(
            self.panel,
            text="Objetos disponibles",
            font=("Arial", 11, "bold"),
            bg=self.COLOR_PANEL, fg=self.COLOR_TEXTO
        ).pack(pady=(20, 5))

        marco_opciones = Frame(self.panel, bg=self.COLOR_PANEL)
        marco_opciones.pack(fill="x", padx=15)

        opciones = [
            "Muro",
            "TorreBasica",
            "TorrePesada",
            "TorreMagica",
            "Soldado",
            "Tanque",
            "UnidadRapida"
        ]

        for opcion in opciones:

            Radiobutton(
                marco_opciones,
                text=opcion,
                variable=self.opcion,
                value=opcion,
                bg=self.COLOR_PANEL,
                fg=self.COLOR_TEXTO,
                selectcolor=self.COLOR_FONDO,
                activebackground=self.COLOR_PANEL,
                activeforeground=self.COLOR_ACENTO,
                font=("Arial", 10),
                anchor="w"
            ).pack(anchor="w", fill="x")

        # ── Boton de pasar fase ──
        btn_pasar = Button(
            self.panel,
            text="Pasar Fase",
            command=self.pasar_fase,
            font=("Arial", 11, "bold"),
            bg="#111111",
            fg="white",
            activebackground=self.COLOR_ACENTO,
            activeforeground="white",
            bd=0,
            relief="flat",
            cursor="hand2"
        )
        btn_pasar.pack(pady=25, padx=15, fill="x")

        btn_pasar.bind("<Enter>", lambda e: btn_pasar.config(bg=self.COLOR_ACENTO))
        btn_pasar.bind("<Leave>", lambda e: btn_pasar.config(bg="#111111"))

        # ── Mensaje de fin de partida ──
        self.lbl_victoria = Label(
            self.panel,
            text="",
            font=("Impact", 14),
            bg=self.COLOR_PANEL,
            fg=self.COLOR_ORO,
            wraplength=260,
            justify="center"
        )
        self.lbl_victoria.pack(pady=10)

    # =====================================
    # CLICK MAPA
    # =====================================

    def click_mapa(self, event):

        if self.partida.finalizada:
            return

        fila = event.y // self.tam_celda
        columna = event.x // self.tam_celda

        opcion = self.opcion.get()

        # =====================
        # DEFENSOR
        # =====================

        if self.partida.fase == "DEFENSOR":

            if opcion == "Muro":
                self.partida.colocar_muro(
                    Muro(),
                    fila,
                    columna
                )

            elif opcion == "TorreBasica":
                self.partida.colocar_torre(
                    TorreBasica(),
                    fila,
                    columna
                )

            elif opcion == "TorrePesada":
                self.partida.colocar_torre(
                    TorrePesada(),
                    fila,
                    columna
                )

            elif opcion == "TorreMagica":
                self.partida.colocar_torre(
                    TorreMagica(),
                    fila,
                    columna
                )

        # =====================
        # ATACANTE
        # =====================

        elif self.partida.fase == "ATAQUE":

            if opcion == "Soldado":

                self.partida.colocar_unidad(
                    Soldado(),
                    fila,
                    columna
                )

            elif opcion == "Tanque":

                self.partida.colocar_unidad(
                    Tanque(),
                    fila,
                    columna
                )

            elif opcion == "UnidadRapida":

                self.partida.colocar_unidad(
                    UnidadRapida(),
                    fila,
                    columna
                )

    # =====================================
    # IMAGENES POR FACCION
    # =====================================

    def nombre_tipo(self, obj):
        """
        Devuelve el nombre de tipo en minuscula usado para construir
        el nombre del archivo de imagen (ej: 'torrebasica', 'soldado').
        """

        if isinstance(obj, Base):
            return "base"

        return obj.__class__.__name__.lower()

    def obtener_imagen(self, tipo, faccion):
        """
        Carga (con cache) la imagen Recursos/Imagenes/<tipo>_<faccion>.png
        redimensionada al tamaño de celda actual. Si el archivo no existe
        o no se puede abrir, devuelve None y quien llama debe usar un
        color de relleno como respaldo.
        """

        clave = f"{tipo}_{faccion}".lower()

        if clave in self.cache_imagenes:
            return self.cache_imagenes[clave]

        nombre_archivo = f"{tipo.lower()}_{faccion.lower()}.png"
        ruta = os.path.join(self.CARPETA_IMAGENES, nombre_archivo)

        imagen_tk = None

        if os.path.isfile(ruta):

            try:
                imagen = Image.open(ruta).convert("RGBA")
                imagen = imagen.resize(
                    (self.tam_celda, self.tam_celda),
                    Image.LANCZOS
                )
                imagen_tk = ImageTk.PhotoImage(imagen)

            except Exception:
                imagen_tk = None

        self.cache_imagenes[clave] = imagen_tk

        return imagen_tk

    # =====================================
    # DIBUJAR FONDO (una sola vez)
    # =====================================

    def dibujar_fondo_mapa(self):

        mapa = self.partida.mapa

        for fila in range(mapa.size):

            for columna in range(mapa.size):

                x1 = columna * self.tam_celda
                y1 = fila * self.tam_celda

                x2 = x1 + self.tam_celda
                y2 = y1 + self.tam_celda

                rect_id = self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=self.COLOR_CELDA,
                    outline=self.COLOR_BORDE_CELDA
                )

                self.celdas_fondo[(fila, columna)] = rect_id
                self.celdas_objeto[(fila, columna)] = None

    # =====================================
    # DIBUJAR (solo actualiza lo que cambio)
    # =====================================

    def dibujar_mapa(self):

        mapa = self.partida.mapa

        colores_def = mapa.facciones.get(
            self.partida.faccion_defensor, {}
        )
        colores_atk = mapa.facciones.get(
            self.partida.faccion_atacante, {}
        )

        for fila in range(mapa.size):

            for columna in range(mapa.size):

                # Si en una ronda nueva el grid cambio de tamaño o se
                # reinicio, nos asegura tener fondo dibujado para esta celda
                if (fila, columna) not in self.celdas_fondo:
                    continue

                obj = mapa.obtener_objeto(fila, columna)

                objeto_anterior_id = self.celdas_objeto.get((fila, columna))

                if objeto_anterior_id is not None:
                    self.canvas.delete(objeto_anterior_id)
                    self.celdas_objeto[(fila, columna)] = None

                if obj is None:
                    continue

                x1 = columna * self.tam_celda
                y1 = fila * self.tam_celda
                x2 = x1 + self.tam_celda
                y2 = y1 + self.tam_celda
                cx = (x1 + x2) // 2
                cy = (y1 + y2) // 2

                tipo = self.nombre_tipo(obj)

                # La base y los muros/torres son del defensor; las unidades
                # son del atacante. Asi se elige la faccion correcta.
                if tipo in ("base", "muro") or "torre" in tipo:
                    faccion = self.partida.faccion_defensor
                else:
                    faccion = self.partida.faccion_atacante

                imagen_tk = self.obtener_imagen(tipo, faccion)

                nuevo_id = None

                if imagen_tk is not None:

                    nuevo_id = self.canvas.create_image(
                        cx, cy,
                        image=imagen_tk
                    )

                else:

                    # Respaldo en color solido si la imagen no existe
                    if tipo == "base":

                        color = colores_def.get("base", self.COLOR_ALERTA)

                        nuevo_id = self.canvas.create_rectangle(
                            x1 + 3, y1 + 3, x2 - 3, y2 - 3,
                            fill=color, outline=""
                        )

                    elif tipo == "muro":

                        color = colores_def.get("muro", "#696969")

                        nuevo_id = self.canvas.create_rectangle(
                            x1 + 5, y1 + 5, x2 - 5, y2 - 5,
                            fill=color, outline=""
                        )

                    elif "torre" in tipo:

                        color = colores_def.get("torre", self.COLOR_ACENTO)

                        nuevo_id = self.canvas.create_oval(
                            x1 + 5, y1 + 5, x2 - 5, y2 - 5,
                            fill=color, outline=""
                        )

                    else:

                        color = colores_atk.get("unidad", "#7CFC00")

                        nuevo_id = self.canvas.create_oval(
                            x1 + 10, y1 + 10, x2 - 10, y2 - 10,
                            fill=color, outline=""
                        )

                self.celdas_objeto[(fila, columna)] = nuevo_id

    # =====================================
    # ACTUALIZAR UI
    # =====================================

    def actualizar_ui(self):

        self.lbl_ronda.config(
            text=f"Ronda {self.partida.ronda}"
        )

        self.lbl_fase.config(
            text=f"Fase: {self.partida.fase}"
        )

        self.lbl_score.config(
            text=(
                f"Defensor {self.partida.victorias_defensor}"
                f"  -  "
                f"{self.partida.victorias_atacante} Atacante"
            )
        )

        vida_base = self.partida.mapa.base.vida

        self.lbl_base.config(
            text=f"Vida de la Base: {vida_base}",
            fg=self.COLOR_ALERTA if vida_base < 250 else self.COLOR_TEXTO
        )

        self.lbl_oro_def.config(
            text=f"Oro Defensor: {self.partida.oro_defensor}"
        )

        self.lbl_oro_atk.config(
            text=f"Oro Atacante: {self.partida.oro_atacante}"
        )

        self.dibujar_mapa()

    # =====================================
    # LOOP
    # =====================================

    def loop(self):

        self.partida.actualizar()

        self.actualizar_ui()

        if self.partida.finalizada:

            self.lbl_victoria.config(
                text=f"¡VICTORIA!\n{self.partida.ganador.nombre}"
            )

            self.mostrar_ventana_victoria()

            return

        self.root.after(
            300,
            self.loop
        )

    # =====================================
    # VENTANA DE VICTORIA
    # =====================================

    def mostrar_ventana_victoria(self):

        ventana = Toplevel(self.root)
        ventana.title("Fin de la partida")
        ventana.configure(bg=self.COLOR_PANEL)
        ventana.geometry("360x220")
        ventana.resizable(False, False)

        Label(
            ventana,
            text="¡PARTIDA FINALIZADA!",
            font=("Impact", 18),
            bg=self.COLOR_PANEL,
            fg=self.COLOR_ACENTO
        ).pack(pady=(25, 10))

        Label(
            ventana,
            text=f"Ganador: {self.partida.ganador.nombre}",
            font=("Arial", 14, "bold"),
            bg=self.COLOR_PANEL,
            fg=self.COLOR_ORO
        ).pack(pady=5)

        Label(
            ventana,
            text=(
                f"Marcador final: "
                f"{self.partida.victorias_defensor} - "
                f"{self.partida.victorias_atacante}"
            ),
            font=("Arial", 11),
            bg=self.COLOR_PANEL,
            fg=self.COLOR_TEXTO
        ).pack(pady=5)

        Button(
            ventana,
            text="Cerrar",
            command=ventana.destroy,
            font=("Arial", 11, "bold"),
            bg="#111111",
            fg="white",
            activebackground=self.COLOR_ACENTO,
            activeforeground="white",
            bd=0,
            relief="flat",
            cursor="hand2"
        ).pack(pady=20)