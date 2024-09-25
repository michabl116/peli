import random
import string

def generar_codigo():
    caracteres = string.ascii_letters + string.digits  # Letras y números
    codigo = ''.join(random.choice(caracteres) for _ in range(4))  # Genera una secuencia de 4 caracteres
    return codigo

# Ejemplo de uso
codigo_aleatorio = generar_codigo()
print("Código aleatorio:", codigo_aleatorio)