from random import randint


def prs(): 
  return randint(0,2)


print("Bienvenido a piedra, papel o tijera")
computer=prs()

human_number=-1
while human_number==-1:
  human=input("Cual vas a usar? ").lower()
  if human=="piedra":
    human_number=0
  elif human=="papel":
    human_number=1
  elif human=="tijera":
    human_number=2
  else:
    print("Opción incorrecta")
    human_number=-1

game = ["""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """,
        """
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """,
        """
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """]

print("Has usado")
print(game[human_number])
print("Tu oponente saca")
print(game[computer])
if human_number==computer:
  print("Empate")
elif (human_number == 0 and computer == 2) or \
    (human_number == 1 and computer == 0) or \
    (human_number == 0 and computer == 2):
    print("Ganaste")
else:
  print("Perdiste")