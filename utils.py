#!/usr/bin/env python3
"""Contiene funciones auxiliares para el funcionamiento del juego."""

import random
from pathlib import Path


def get_random_word():
    """Lee las palabras del archivo y devuelve una seleccionada al azar."""

    # Obtener la ubicación del archivo wordlist.txt
    ruta_archivo = Path(__file__).resolve().parent / "wordlist.txt"

    # Abrir el archivo y leer todas sus líneas
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        palabras = []

        for linea in archivo:
            palabra = linea.strip()

            # Comprobar que contenga letras y espacios solamente
            if palabra and any(letra.isalpha() for letra in palabra):
                if all(letra.isalpha() or letra.isspace()
                       for letra in palabra):
                    palabras.append(palabra)

    # Comprobar que existan palabras disponibles
    if not palabras:
        raise ValueError("No hay palabras válidas en wordlist.txt")

    # Seleccionar y devolver una palabra aleatoria
    return random.choice(palabras)
