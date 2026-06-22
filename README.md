# Defensa y Asalto de Base

## Descripción

**Defensa y Asalto de Base** es un videojuego de estrategia por turnos para dos jugadores, desarrollado en Python utilizando Tkinter para la interfaz gráfica. Un jugador asume el rol de **Defensor**, colocando muros y torres para proteger su base, mientras el otro jugador asume el rol de **Atacante**, desplegando unidades (soldados, tanques y unidades rápidas) para destruirla.

El sistema incluye:

- Pantalla de **menú principal** con navegación entre módulos.
- Sistema de **login** para registrar y seleccionar jugadores.
- Selección de **facciones** con recursos gráficos diferenciados.
- Lógica de partida por **fases** (colocación y combate) gestionada en rondas.
- Pantalla de **ranking** con historial de victorias.
- Persistencia de datos de jugadores en formato **JSON**.

---

## Requisitos

- **Python 3.10 o superior**
- Librerías estándar utilizadas: `tkinter`, `json`, `os`
- Dependencia externa:
  - **Pillow** (manejo de imágenes de facciones)

### Instalación de la dependencia externa

```bash
pip install pillow
```

> Tkinter y json ya vienen incluidos con la instalación estándar de Python, no requieren instalación adicional.

---

## Estructura del proyecto

```
Defensa-y-Asalto-de-Base/
│
├── main.py                  # Archivo principal de ejecución
│
├── Clases/                  # Lógica del juego (modelo)
│   ├── Jugador.py
│   ├── Partida.py
│   ├── Mapa.py
│   ├── Base.py
│   ├── Muro.py
│   ├── Torre.py
│   ├── TorreBasica.py
│   ├── TorrePesada.py
│   ├── TorreMagica.py
│   ├── Soldado.py
│   ├── Tanque.py
│   ├── Unidad.py
│   └── UnidadRapida.py
│
├── Interfaz/                 # Pantallas e interfaz gráfica (vista)
│   ├── Menu.py
│   ├── Login.py
│   ├── Juego.py
│   ├── Ranking.py
│   └── PantallaVictoria.py
│
├── Recursos/
│   └── Imagenes/             # Imágenes de facciones, unidades y fondo
│
├── Datos/
│   └── jugadores.json        # Almacenamiento de datos de jugadores
│
└── README.md
```

---

## Instrucciones de ejecución

El proyecto **no requiere compilación ni instalación adicional** más allá de Pillow. Se ejecuta directamente con Python desde la carpeta raíz del proyecto:

```bash
python main.py
```

> **Importante:** el comando debe ejecutarse siempre desde la carpeta raíz del proyecto (la que contiene `main.py`), ya que las rutas hacia `Recursos/` y `Datos/` son relativas a esa ubicación.

---

## Almacenamiento de datos (JSON)

Los datos de los jugadores (nombre y estadísticas de victorias) se almacenan en el archivo:

```
Datos/jugadores.json
```

Cada vez que se registra un jugador nuevo o finaliza una partida, el sistema:

1. **Lee** el archivo JSON existente (si ya hay datos guardados).
2. **Actualiza** la información correspondiente en memoria (por ejemplo, suma una victoria).
3. **Escribe** nuevamente el archivo completo con los datos actualizados.

Esto permite que el ranking y los perfiles de jugador persistan entre distintas ejecuciones del programa, sin necesidad de una base de datos externa.

> Si el archivo `jugadores.json` no existe al iniciar el programa, este se crea automáticamente con una estructura vacía.

---

## Recursos gráficos

Las imágenes utilizadas en la interfaz (fondo del menú, unidades, torres y muros por facción) se encuentran en:

```
Recursos/Imagenes/
```

Las imágenes de unidades y estructuras siguen la convención de nombre:

```
<tipo>_<faccion>.png
```

Por ejemplo: `torrebasica_medieval.png`, `soldado_futurista.png`.

Si una imagen no se encuentra en la carpeta, el programa no se detiene: utiliza automáticamente un color de relleno como respaldo visual.

---

## Notas importantes para evitar errores comunes

- **Ejecutar siempre desde la carpeta raíz del proyecto.** Si se ejecuta `main.py` desde otra ubicación, las rutas relativas hacia `Recursos/` y `Datos/` no se resolverán correctamente.
- **No mover ni renombrar las carpetas** `Clases/`, `Interfaz/`, `Recursos/` o `Datos/`, ya que el código depende de estos nombres exactos.
- **Instalar Pillow antes de ejecutar el programa.** Sin esta librería, el módulo de interfaz del juego (`Juego.py`) no podrá importarse.
- **No editar manualmente `jugadores.json`** salvo que se conozca su estructura interna, ya que un formato inválido puede impedir que el programa cargue los datos al iniciar.
- Si aparece un error de tipo `FileNotFoundError` relacionado con imágenes, verificar que los archivos `.png` existan dentro de `Recursos/Imagenes/` con el nombre exacto esperado.

---

## Autoría

Proyecto desarrollado como parte de un curso universitario de introducción a la programación, con fines académicos por los estudiantes Gabriel Montero Garro y Esteban Solano Orozco.