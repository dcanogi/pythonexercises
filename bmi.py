from colorama import init, Fore
init(autoreset=True)

height = int(input("Dime tu altura en centímetros: "))
weight = int(input("Dime tu peso en KG: "))
height = height / 100
height = height ** 2
result = round(weight / height, 2)

print("Tu IMC o BMI es", result)

if result < 18.5:
    print(f"Categoría: {Fore.BLUE}Bajo peso{Fore.RESET}")
elif 18.5 <= result < 25:
    print(f"Categoría: {Fore.GREEN}Normal{Fore.RESET}")
elif 25 <= result < 30:
    print(f"Categoría: {Fore.YELLOW}Sobrepeso{Fore.RESET}")
else:
    print(f"Categoría: {Fore.RED}Obesidad{Fore.RESET}")
