from random import randint
from colorama import init, Fore, Back, Style

# Inicializar colorama
init()

def text_to_array(texto):
    return list(texto)

end = False
words = ('abeja babuino tejón murciélago oso castor camello gato almeja cobra puma '
   'coyote cuervo ciervo perro burro pato águila hurón zorro rana cabra '
   'ganso halcón león lagarto llama topos mono alce ratón mula salamandra '
   'nutria búho panda loro paloma pitón conejo carnero rata cuervo '
   'rinoceronte salmón foca tiburón oveja mofeta perezoso serpiente '
   'araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena '
   'lobo wombat cebra').split()
words = words[randint(0, 63)]
secret = ["-" for _ in range(len(words))]
array_word = text_to_array(words)
HANGMANPICS = [f'''
  +---+
  |   |
      |
      |
      |
      |
=========''', f'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', f'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', f'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', f'''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', f'''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', f'''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']
hangman = 0

while not end:

    print(f"""
    {Fore.BLUE}
    ('-. .-.   ('-.         .-') _            _   .-')      ('-.         .-') _  
    ( OO )  /  ( OO ).-.    ( OO ) )          ( '.( OO )_   ( OO ).-.    ( OO ) ) 
    ,--. ,--.  / . --. /,--./ ,--,'  ,----.    ,--.   ,--.) / . --. /,--./ ,--,'  
    |  | |  |  | \-.  \ |   \ |  |\ '  .-./-') |   `.'   |  | \-.  \ |   \ |  |\  
    |   .|  |.-'-'  |  ||    \|  | )|  |_( O- )|         |.-'-'  |  ||    \|  | ) 
    |       | \| |_.'  ||  .     |/ |  | .--, \|  |'.'|  | \| |_.'  ||  .     |/  
    |  .-.  |  |  .-.  ||  |\    | (|  | '. (_/|  |   |  |  |  .-.  ||  |\    |   
    |  | |  |  |  | |  ||  | \   |  |  '--'  | |  |   |  |  |  | |  ||  | \   |   
    `--' `--'  `--' `--'`--'  `--'   `------'  `--'   `--'  `--' `--'`--'  `--'   
    {Style.RESET_ALL}""")
    print("""
    Bienvenido a hangman:
    Las reglas son fáciles, no la lies y no morirá
    """)
    print(' '.join(secret))
    print(HANGMANPICS[hangman])
    guess = input("Dime una letra: ").lower()
    pointer = 0
    for i, e in enumerate(array_word):
        if guess == e:
            secret[i] = e
            pointer += 1
    if pointer == 0:
        hangman += 1

    if hangman == 6:
        print(f"{Fore.RED}¡Oh no! Has alcanzado el límite de intentos. La palabra era: {words}{Style.RESET_ALL}")
        end = True
    elif "-" not in secret:
        print(f"{Fore.GREEN}¡Felicidades! ¡Has adivinado la palabra: {words}{Style.RESET_ALL}")
        end = True

