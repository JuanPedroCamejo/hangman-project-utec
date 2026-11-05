
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

    def process_guess(self, letter):
        """
        Procesa la letra ingresada por el usuario.
        - Si está en la palabra (ignorando mayúsculas/minúsculas), la agrega a guessed_letters.
        - Si no está, incrementa el contador de errores.
        - Devuelve True si fue correcta, False si fue incorrecta.
        """
        # Asegurarnos de trabajar con minúsculas para la comparación
        letter_lower = letter.lower()
        word_lower = self.word.lower()

        # Comprobar pertenencia usando 'in'
        if letter_lower in word_lower:
            if letter_lower not in self.guessed_letters:
                self.guessed_letters.append(letter_lower)
            return True
        else:
            # Si no está en la palabra y no se había registrado como error previo (opcional)
            self.errors += 1
            if letter_lower not in self.guessed_letters:
                self.guessed_letters.append(letter_lower)
            return False
