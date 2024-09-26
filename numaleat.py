import random

def centros_cuadrados(seed, n):
    """Genera n números pseudoaleatorios por el método de centros cuadrados"""
    numeros = []
    for _ in range(n):
        seed_cuadrado = str(seed ** 2).zfill(8)  
        seed = int(seed_cuadrado[2:6])  
        numero = (seed % 100) + 1  
        numeros.append(numero)
    return numeros

def medios_cuadrados(seed, n):
    """Genera n números pseudoaleatorios por el método de medios cuadrados"""
    numeros = []
    for _ in range(n):
        seed_cuadrado = str(seed ** 2).zfill(8)  
        seed = int(seed_cuadrado[2:6])  
        seed += random.randint(1, 100)  
        numero = (seed % 100) + 1  
        numeros.append(numero)
    return numeros

seed_inicial = 1234 

numeros_centros_cuadrados = centros_cuadrados(seed_inicial, 100)

numeros_medios_cuadrados = medios_cuadrados(seed_inicial, 100)

print("Números generados por Centros Cuadrados:")
print(numeros_centros_cuadrados)

print("\nNúmeros generados por Medios Cuadrados:")
print(numeros_medios_cuadrados)

