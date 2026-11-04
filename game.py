
#!/usr/bin/env python3
"""Contiene la clase principal que administra el juego del ahorcado."""


class HangmanGame:
    """Gestiona el estado y el progreso del juego."""

    def __init__(self, word):
        """Inicializa los atributos del juego."""

        self.word = word
        self.guessed_letters = []
        self.max_errors = 6
        self.errors = 0

    def display_progress(self):
        """Muestra las letras adivinadas y oculta las restantes."""

        progreso = []

        for letra in self.word:
            if letra.isalpha():
                if letra.lower() in self.guessed_letters:
                    progreso.append(letra)
                else:
                    progreso.append("_")
            else:
                progreso.append(letra)

        print(" ".join(progreso))
