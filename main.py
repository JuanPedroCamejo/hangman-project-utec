
#!/usr/bin/env python3


from game import HangmanGame
from utils import get_random_word


def mostrar_estado(juego):
    """Muestra el progreso, las letras intentadas y los intentos restantes."""

    print("\n----------------------------------------")

    print("Progreso actual: ", end="")
    juego.display_progress()

    print(f"Letras intentadas: {juego.guessed_letters}")

    intentos_restantes = juego.max_errors - juego.errors
    print(f"Intentos incorrectos restantes: {intentos_restantes} / "
          f"{juego.max_errors}")


def main():
    """Ejecuta el juego del ahorcado."""

    print("Bienvenido al juego del Ahorcado")

    palabra_secreta = get_random_word()
    juego = HangmanGame(palabra_secreta)

    while juego.errors < juego.max_errors:

        mostrar_estado(juego)

        letra_valida = None

        while letra_valida is None:
            entrada = input("Ingresa una letra: ").strip().lower()

            if len(entrada) != 1 or not entrada.isalpha():
                print("Error: Debes ingresar una sola letra "
                      "valida (sin numeros ni simbolos).")
                continue

            if entrada in juego.guessed_letters:
                print(f"Ya habias intentado la letra '{entrada}'. "
                      "Prueba con otra.")
                continue

            letra_valida = entrada

        es_correcta = juego.process_guess(letra_valida)

        if es_correcta:
            print(f"Bien hecho! La letra '{letra_valida}' esta en la palabra.")
        else:
            print(f"La letra '{letra_valida}' no esta en la palabra.")

        if all(letra in juego.guessed_letters
               for letra in juego.word.lower()
               if letra.isalpha()):

            mostrar_estado(juego)

            print("\nFelicitaciones! Has ganado el juego.")
            print(f"La palabra secreta era: {juego.word}")
            return

    mostrar_estado(juego)

    print("\nGame Over! Te has quedado sin intentos.")
    print(f"La palabra secreta era: {juego.word}")


if __name__ == "__main__":
    main()
