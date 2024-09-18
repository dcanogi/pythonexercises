print("Bienvenido a la pizzeria Cano")
size = input("¿De qué tamaño quieres la pizza? (S, M, L) ")
add_pepperoni = input("¿Quieres pepperoni? (S/N) ")
extra_cheese = input("¿Extra de queso? (S/N) ")
bill = 0
if size.lower() == "s":
    bill = 15
elif size.lower() == "m":
    bill = 20
elif size.lower() == "l":
    bill = 25
else:
    print("Vuelve a intentarlo")
if add_pepperoni.lower() == "s":
    bill += 2 if size.lower() == "s" else 3
if extra_cheese.lower() == "s":
    bill += 1

print(f"Total a pagar: {bill}€")
