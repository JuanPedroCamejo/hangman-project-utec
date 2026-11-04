# Hangman Project – UTEC

## Descripción

Proyecto académico desarrollado en Python para implementar el clásico juego del ahorcado.

El objetivo es construir un juego por consola en el que el usuario debe adivinar una palabra o frase seleccionada aleatoriamente desde un archivo de texto.

El proyecto se desarrolla de forma modular, utilizando funciones, clases, manejo de archivos y validación de entradas.

## Estructura del proyecto

```text
hangman_project/
│
├── main.py          # Punto de entrada del programa
├── game.py          # Clase principal y lógica del juego
├── utils.py         # Funciones auxiliares
├── wordlist.txt     # Lista de palabras y frases
├── README.md        # Documentación del proyecto
└── .gitignore       # Archivos que Git debe ignorar
```

## Requisitos

- Python 3 instalado.
- Git instalado.
- Visual Studio Code (recomendado).

No es necesario instalar paquetes externos para las funcionalidades implementadas hasta el momento, ya que se utilizan módulos de la biblioteca estándar de Python.

## Funcionalidades implementadas

### Tarea 1: Selección aleatoria de palabras

Archivo: `utils.py`

Se implementó la función `get_random_word()`, que:

- Lee las palabras y frases almacenadas en `wordlist.txt`.
- Elimina espacios innecesarios al principio y al final de cada línea.
- Comprueba que las entradas contengan letras y espacios.
- Selecciona una entrada aleatoria utilizando `random.choice()`.
- Devuelve la palabra o frase seleccionada.

### Tarea 2: Clase HangmanGame

Archivo: `game.py`

Se creó la clase `HangmanGame`, que administra el estado del juego.

Atributos:

- `word`: palabra o frase que debe adivinarse.
- `guessed_letters`: lista de letras adivinadas.
- `max_errors`: máximo de errores permitidos (6).
- `errors`: contador de respuestas incorrectas (inicialmente 0).

Método:

- `display_progress()`: muestra las letras adivinadas en sus posiciones correspondientes y oculta las restantes mediante guiones bajos. Los espacios y signos de puntuación se muestran automáticamente.

## Pruebas desde PowerShell

Abrir PowerShell y ubicarse en la carpeta del proyecto:

```powershell
cd "$env:USERPROFILE\Desktop\hangman_project"
```

### 1. Probar la selección aleatoria de palabras

Ejecutar:

```powershell
python -c "from utils import get_random_word; print(get_random_word())"
```

Resultado esperado:

Se muestra una palabra o frase existente en `wordlist.txt`.

Ejecutar el comando varias veces para comprobar que la selección puede variar.

### 2. Probar la clase HangmanGame

Ejecutar:

```powershell
python -c "from game import HangmanGame; juego = HangmanGame('elephant'); juego.guessed_letters = ['e', 'a']; juego.display_progress()"
```

Resultado esperado:

```text
e _ e _ _ a _ _
```

Esta prueba comprueba que se muestran las letras adivinadas y se ocultan las restantes.

### 3. Comprobar los atributos de la clase

Ejecutar:

```powershell
python -c "from game import HangmanGame; juego = HangmanGame('elephant'); print(juego.word); print(juego.guessed_letters); print(juego.max_errors); print(juego.errors)"
```

Resultado esperado:

```text
elephant
[]
6
0
```

Esto permite verificar los valores iniciales de los cuatro atributos.

## Archivos ignorados por Git

El archivo `.gitignore` contiene:

```gitignore
__pycache__/
*.py[cod]
```

Estas reglas evitan subir a GitHub los archivos temporales y compilados que Python genera automáticamente.

## Tecnologías utilizadas

- Python 3.
- Git y GitHub.
- Visual Studio Code.
- PowerShell.

## Estado del proyecto

Proyecto en desarrollo. Las tareas se implementan y prueban progresivamente hasta completar el juego del ahorcado.

## Repositorio

[Hangman Project – GitHub](https://github.com/JuanPedroCamejo/hangman-project-utec.git)
