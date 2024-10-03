import time


def print_with_delay(text):
    pause = 0.2  # Pausa fija de 0.2 segundos
    character_limit = 50  # Límite de caracteres fijo
    text2 = text.split()  # Divide el texto en palabras
    character_counter = 0  # Contador de caracteres para cada línea

    for word in text2:
        # Si la siguiente palabra excede el límite de caracteres, imprime un salto de línea
        if character_counter + len(word) > character_limit:
            print()  # Salto de línea
            character_counter = 0  # Reinicia el contador de caracteres

        # Imprime la palabra con un espacio al final y actualiza el contador de caracteres
        print(word, end=' ', flush=True)
        character_counter += len(word) + 1  # +1 para incluir el espacio
        time.sleep(pause)  # Pausa entre las palabras

    print()