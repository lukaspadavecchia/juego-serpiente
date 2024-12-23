# Ta-Te-Ti Moderno

Un juego de Ta-Te-Ti (Tic-tac-toe) moderno implementado en Python con una interfaz de línea de comandos colorida y atractiva.

## Características

- Interfaz colorida y moderna usando la biblioteca colorama
- Diseño modular y bien estructurado
- Validación de movimientos
- Sistema de turnos intuitivo
- Detección automática de ganador
- Opción para jugar múltiples partidas

## Requisitos

- Python 3.6 o superior
- Biblioteca colorama

## Cómo jugar

1. Ejecuta el juego con:
   ```
   python main.py
   ```

2. El juego mostrará un tablero 3x3 donde:
   - Jugador 1 usa X (cyan)
   - Jugador 2 usa O (magenta)

3. Para hacer un movimiento:
   - Ingresa la fila y columna separadas por un espacio
   - Por ejemplo: "2 3" para la fila 2, columna 3
   - Las filas y columnas van del 1 al 3

4. El juego termina cuando:
   - Un jugador gana al alinear tres símbolos
   - El tablero se llena (empate)

5. Puedes elegir jugar otra partida al finalizar

## Estructura del proyecto

```
├── main.py
├── game/
│   ├── board.py
│   ├── display.py
│   └── game_manager.py
└── README.md
```

## Contribuir

¡Las contribuciones son bienvenidas! Si tienes alguna idea para mejorar el juego, no dudes en:

1. Hacer un fork del repositorio
2. Crear una rama para tu feature
3. Hacer commit de tus cambios
4. Crear un pull request

## Licencia

Este proyecto está bajo la Licencia MIT.