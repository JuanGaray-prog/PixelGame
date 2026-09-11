=========================================
PROYECTO: SNAKE GAME (PIXEL ART - POO)
=========================================

1. REQUISITOS DEL SISTEMA
-------------------------
- Python 3.8 o superior
- Pygame >= 2.5.0

Instalación de dependencias:
> pip3 install pygame

(O mediante requirements.txt: pip3 install -r requirements.txt)


2. ESTRUCTURA DEL PROYECTO
--------------------------
PixelGame/
│
├── assets/                  # Guardar aquí todas las imágenes y sprites
│   ├── Head.png
│   ├── Head_red.png
│   ├── Body.jpg
│   ├── Body_red.jpg
│   ├── Body_curve.png
│   ├── Body_curve_red.png
│   ├── Tail.png
│   ├── Tail_red.png
│   ├── Manzana.png
│   ├── Menu.png
│   ├── Play.png
│   └── Winner.png
│
├── src/                    # Código fuente modular
│   ├── core/
│   │   └── game.py          # Control del bucle principal y estados del juego
│   ├── entities/
│   │   ├── snake.py         # Lógica, cuerpo y movimiento de las serpientes
│   │   └── food.py          # Posicionamiento y renderizado de la manzana
│   ├── graphics/
│   │   └── renderer.py      # Renderizado del tablero y mensajes de interfaz
│   └── utils/
│       └── constants.py     # Dimensiones, colores y mapeo de controles
│
├── main.py                  # Punto de entrada para iniciar la aplicación
└── requirements.txt         # Lista de librerías necesarias


3. INSTRUCCIONES DE EJECUCIÓN
-----------------------------
Abre la terminal en la carpeta principal del proyecto y ejecuta:

- En macOS / Linux:
  python3 main.py

- En Windows:
  python main.py


4. CONTROLES
------------
- Jugador 1 (Serpiente Azul): Flechas de dirección (Arriba, Abajo, Izquierda, Derecha)
- Jugador 2 (Serpiente Roja): Teclas W, A, S, D