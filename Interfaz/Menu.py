import os
from tkinter import *


ventana = Tk()
ventana.title("Defensa y Asalto de Base")

canvas = Canvas(
    ventana,
    width=1200,
    height=600,
    bg="black",
    highlightthickness=0
)
canvas.pack()


def limpiar_pantalla():
    canvas.delete("all")


def ajustar_ventana(ancho, alto):
    ventana.geometry(f"{ancho}x{alto}")
    canvas.config(
        width=ancho,
        height=alto
    )


def crear_boton(texto, accion):

    btn = Button(
        ventana,
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

    def entrar(event):
        btn.config(bg="#001F63", fg="white")

    def salir(event):
        btn.config(bg="#111111", fg="white")

    btn.bind("<Enter>", entrar)
    btn.bind("<Leave>", salir)

    return btn


def iniciar_juego():
    print("Iniciar juego")


def mostrar_estadisticas():
    print("Mostrar estadísticas")


def salir():
    ventana.destroy()


def mostrar_menu():

    ajustar_ventana(1200, 600)
    limpiar_pantalla()

    ruta_imagen = os.path.join(
        os.path.dirname(__file__),
        "..",
        "Recursos",
        "Imagenes",
        "main_background.png"
    )

    try:
        fondo = PhotoImage(file=ruta_imagen)
        canvas.fondo = fondo
        canvas.create_image(0, 0, image=fondo, anchor="nw")
    except:
        canvas.config(bg="black")

    centro_x = 600

    # ── Panel principal ──
    canvas.create_rectangle(
        275, 50, 900, 450,
        fill="#111111",
        outline="#001F63",
        width=3
    )

    # ── Esquinas decorativas tipo HUD ──
    esquinas = [(275, 50), (900, 50), (275, 450), (900, 450)]
    for x, y in esquinas:
        canvas.create_line(x - 12, y, x + 12, y, fill="#3A7BFF", width=2)
        canvas.create_line(x, y - 12, x, y + 12, fill="#3A7BFF", width=2)

    # ── Título ──
    canvas.create_text(
        centro_x, 130,
        text="DEFENSA Y ASALTO DE BASE",
        fill="#3A7BFF",
        font=("Impact", 36)
    )

    # ── Botones ──
    btn_jugar = crear_boton("Jugar", iniciar_juego)
    btn_estadisticas = crear_boton("Estadísticas", mostrar_estadisticas)
    btn_salir = crear_boton("Salir", salir)

    canvas.create_window(centro_x, 250, window=btn_jugar)
    canvas.create_window(centro_x, 320, window=btn_estadisticas)
    canvas.create_window(centro_x, 390, window=btn_salir)
