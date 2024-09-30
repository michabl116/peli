import time
texto =

palabras = texto.split()

pausa = 0.5

limite_caracteres = 50

contador_caracteres = 0


for palabra in palabras:

    if contador_caracteres + len(palabra) > limite_caracteres:
        print()
        contador_caracteres = 0


    print(palabra, end=' ', flush=True)


    contador_caracteres += len(palabra) + 1


    time.sleep(pausa)

print()