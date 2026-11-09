# Hangman Project – UTEC

## Descripción

Este proyecto consiste en desarrollar el clásico juego del **Ahorcado (Hangman)** utilizando Python.

El programa selecciona aleatoriamente una palabra o frase desde un archivo de texto (`wordlist.txt`). El jugador debe descubrirla ingresando letras individuales. Cuenta con un máximo de seis intentos incorrectos.

El proyecto está organizado en módulos para separar las responsabilidades y facilitar su mantenimiento.

## Estructura del proyecto

```text
hangman_project/
│
├── main.py          # Punto de entrada y flujo principal del juego
├── game.py          # Clase HangmanGame y lógica del juego
├── utils.py         # Funciones auxiliares
├── wordlist.txt     # Palabras y frases disponibles
├── README.md        # Documentación del proyecto
└── .gitignore       # Archivos excluidos de Git
```

## Requisitos

- Python 3.
- Git.
- Visual Studio Code (recomendado).

No se necesitan instalar dependencias externas.

## Cómo ejecutar el proyecto

1. Clonar el repositorio:

```bash
git clone https://github.com/JuanPedroCamejo/hangman-project-utec.git
```

2. Ingresar a la carpeta:

```bash
cd hangman_project
```

3. Ejecutar el juego:

```bash
python main.py
```

## Funcionalidades implementadas

### Tarea 1 – Selección aleatoria de palabras

Se implementó la función `get_random_word()` en `utils.py`.

Responsabilidades:

- Leer las palabras y frases del archivo `wordlist.txt`.
- Eliminar espacios y saltos de línea al principio y al final mediante `strip()`.
- Validar que cada entrada contenga letras y espacios.
- Ignorar las líneas vacías y las entradas que no cumplen las condiciones.
- Seleccionar una palabra o frase aleatoriamente mediante `random.choice()`.
- Informar mediante una excepción si no existen palabras válidas.

Se utiliza `pathlib.Path` para localizar el archivo independientemente del directorio desde el que se ejecute el programa.

### Tarea 2 – Clase principal del juego

Se implementó la clase `HangmanGame` en `game.py`.

Atributos:

| Atributo | Descripción |
|---|---|
| `word` | Palabra o frase que debe descubrir el jugador. |
| `guessed_letters` | Lista de letras que ya fueron ingresadas. |
| `max_errors` | Cantidad máxima de errores permitidos (6). |
| `errors` | Cantidad de intentos incorrectos realizados. |

Métodos:

- `__init__(word)`: inicializa el estado del juego.
- `display_progress()`: muestra las letras descubiertas y oculta las restantes con guiones bajos.

Los espacios de las frases se mantienen visibles durante toda la partida.

### Tarea 3 – Validación de entradas

Se implementó la validación de las entradas en `main.py`.

El programa comprueba que:

- El jugador ingrese una sola letra.
- No se acepten entradas vacías.
- No se acepten números ni símbolos.
- No se permitan letras que ya fueron ingresadas anteriormente.
- Las letras se conviertan a minúsculas para realizar las comparaciones.

Si la entrada no es válida, se informa el error y se solicita otra letra sin descontar intentos.

### Tarea 4 – Procesamiento de intentos

Se implementó el método `process_guess(letter)` en `game.py`.

Responsabilidades:

- Comprobar si la letra ingresada está presente en la palabra o frase.
- Utilizar el operador `in` para verificar su pertenencia.
- Registrar las letras ingresadas en `guessed_letters`.
- Incrementar `errors` cuando la letra no está presente.
- Devolver `True` cuando la letra es correcta y `False` cuando es incorrecta.

Las comparaciones no distinguen entre mayúsculas y minúsculas.

### Tarea 5 – Visualización del estado del juego

Se implementó la función `mostrar_estado(juego)` en `main.py`.

Esta función muestra:

- El progreso actual de la palabra o frase.
- Las letras que el jugador ya intentó ingresar, tanto correctas como incorrectas.
- La cantidad de intentos incorrectos restantes.

Los intentos restantes se calculan mediante:

```python
intentos_restantes = juego.max_errors - juego.errors
```

La función se utiliza durante la partida y también al finalizarla, para mostrar el estado final tanto en caso de victoria como de derrota.

### Tarea 6 – Verificación de las condiciones de fin del juego

Se implementaron los métodos `is_won()` e `is_lost()` en la clase `HangmanGame`, dentro de `game.py`.

- `is_won()` devuelve `True` cuando todas las letras de la palabra fueron adivinadas.
- `is_lost()` devuelve `True` cuando la cantidad de errores alcanza `max_errors`.
- En `main.py`, el bucle continúa mientras el jugador no haya ganado ni perdido. Al terminar, se muestra el resultado y la palabra secreta.

Al ganar, el juego muestra un mensaje de felicitación. Al perder, informa que se acabaron los intentos.

### Tarea 7 – Revelado automático de caracteres no alfabéticos

Se modificó `display_progress()` en `game.py` para mostrar automáticamente los caracteres que no son letras, como espacios, guiones y signos de puntuación, manteniendo su posición original en la palabra o frase.

Estos caracteres no se deben adivinar y no cuentan para la victoria. `is_won()` comprueba únicamente las letras, mientras que `errors` aumenta solamente cuando se ingresa una letra incorrecta.

Por ejemplo, en `mother-in-law`, los guiones se muestran desde el inicio. Los espacios también permanecen visibles en las frases.

## Pruebas realizadas

Se realizaron pruebas desde PowerShell para comprobar las distintas funcionalidades.

### 1. Comprobar la selección aleatoria

```powershell
python -c "from utils import get_random_word; print(get_random_word())"
```

Permite comprobar que se obtiene una palabra o frase del archivo `wordlist.txt`.

### 2. Comprobar la inicialización de la clase

```powershell
python -c "from game import HangmanGame; juego = HangmanGame('Python'); print(juego.word); print(juego.guessed_letters); print(juego.max_errors); print(juego.errors)"
```

Resultado esperado:

```text
Python
[]
6
0
```

### 3. Comprobar el procesamiento de una letra correcta

```powershell
python -c "from game import HangmanGame; juego = HangmanGame('Python'); print(juego.process_guess('p')); print(juego.guessed_letters); print(juego.errors)"
```

Resultado esperado:

```text
True
['p']
0
```

### 4. Comprobar el procesamiento de una letra incorrecta

```powershell
python -c "from game import HangmanGame; juego = HangmanGame('Python'); print(juego.process_guess('z')); print(juego.guessed_letters); print(juego.errors)"
```

Resultado esperado:

```text
False
['z']
1
```

### 5. Comprobar la ejecución completa

```powershell
python main.py
```

Se realizaron pruebas de partidas ganadas y perdidas, verificando:

- El descubrimiento progresivo de las letras.
- El registro de letras correctas e incorrectas.
- El rechazo de entradas inválidas.
- La prevención de letras repetidas.
- El descuento de intentos incorrectos.
- La finalización al descubrir la palabra.
- La finalización al alcanzar los seis errores.
- La visualización del estado final de la partida.

También se comprobó la sintaxis de los archivos Python mediante:

```powershell
python -m py_compile main.py
```

## Archivo .gitignore

Se utiliza `.gitignore` para evitar subir archivos temporales y archivos compilados de Python.

Contenido:

```gitignore
__pycache__/
*.py[cod]
```

## Tecnologías utilizadas

- **Python 3:** desarrollo de la lógica y funcionalidades del juego.
- **Git:** control de versiones.
- **GitHub:** alojamiento del repositorio.
- **Visual Studio Code:** entorno de desarrollo.
- **PowerShell:** ejecución y pruebas desde Windows.

## Estado del proyecto

Las tareas 1 a 7 se encuentran implementadas y verificadas mediante pruebas desde PowerShell.

El proyecto continúa en desarrollo, sujeto a las próximas consignas y mejoras que se incorporen durante el curso.

## Repositorio

[GitHub – Hangman Project](https://github.com/JuanPedroCamejo/hangman-project-utec)
