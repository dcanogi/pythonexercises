print("Bienvenidos al Cine")
print("""
  Entrada Adultos 10€
  Entrada Niños 8€
  Entrada Tercera Edad 4€

Si quieres palomitas y refresco serán 6€ extra
""")
people = int(input("¿Cuántas entradas quieres?"))
i = 1
bill = 0
while people != 0:
    type_entry = input(f"Para la entrada {i} dime de qué tipo: Adulto, Niño, Tercera Edad: ").lower()
    if type_entry == "adulto":
        bill += 10
        i += 1
        people -= 1
    elif type_entry == "niño":
        bill += 8
        i += 1
        people -= 1
    elif type_entry == "tercera edad":
        bill += 4
        i += 1
        people -= 1
    else:
        print("Por favor, elija un tipo de entrada válido.")

    extra = input("¿Quieres refresco y palomitas? ").lower()
    if extra == "si":
        bill += 6

print(f"En total sería {bill}€")
