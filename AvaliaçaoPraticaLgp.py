import math

def calcular_volume_esfera(raio):
    volume = (4/3) * math.pi * (raio ** 3)
    return volume

raio = float(input("Digite o raio da esfera: "))

volume = calcular_volume_esfera(raio)

print(f"O volume da esfera é {volume:.2f}cm")


