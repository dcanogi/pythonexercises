import string
import random
print("Generador de contraseñas")
passwd=[]
chars=int(input("Cuantas letras quieres? "))
for i in range(chars):
  passwd.append(random.choice(string.ascii_letters))
  i=+1
symbols=int(input("Cuantos símbolos quieres? "))
for i in range(symbols):
  passwd.append(random.choice(string.punctuation))
  i=+1
numbers=int(input("Cuantos números quieres? "))
for i in range(numbers):
  passwd.append(random.randint(0,9))
  i=+1
  random.shuffle(passwd)
result= ''.join(str(x) for x in passwd)
print(f"Tu nueva contraseña es: {result}")