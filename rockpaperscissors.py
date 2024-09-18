import random

print("Bienvenido a Piedra, Papel o Tijera")
opciones = ["piedra", "papel", "tijera"]
player = input("Selecciona uno para luchar contra mí: ").lower()
computer = random.choice(opciones)

print(f"Saco {computer}")

if player == computer:
    print("Empate")
elif (player == "piedra" and computer == "tijera") or \
        (player == "papel" and computer == "piedra") or \
        (player == "tijera" and computer == "papel"):
    print("¡Ganaste!")
else:
    print("¡Perdiste!")
