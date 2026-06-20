from Clases.Jugador import Jugador

# ── DATOS DE PRUEBA ──
defensores = [
    ("Ana", 5),
    ("Luis", 2),
    ("Carlos", 8),
    ("Maria", 1),
    ("Jose", 4),
    ("Sofia", 10),
    ("Pedro", 3),
    ("Elena", 7),
    ("Diego", 6),
    ("Laura", 9)
]

atacantes = [
    ("Ana", 3),
    ("Luis", 8),
    ("Carlos", 1),
    ("Maria", 6),
    ("Jose", 2),
    ("Sofia", 4),
    ("Pedro", 9),
    ("Elena", 5),
    ("Diego", 7),
    ("Laura", 10)
]

# ── CREAR Y GUARDAR ──

#e: ninguna
#s: ninguna
# Crea jugadores de prueba y actualiza sus victorias en el archivo
for i in range(10):
    nombre = defensores[i][0]
    vict_def = defensores[i][1]
    vict_ata = atacantes[i][1]

    # intentar registrar usuario (si ya existe no lo duplica)
    Jugador.registrar_en_archivo(nombre, "123")

    # cargar jugador
    jugador = Jugador.iniciar_sesion(nombre, "123")

    if jugador:
        jugador.victorias_defensor = vict_def
        jugador.victorias_atacante = vict_ata
        jugador.guardar_victorias()

print("✔ 10 jugadores creados y actualizados correctamente")