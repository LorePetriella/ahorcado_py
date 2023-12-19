import random


lives = 10
wrong_letters = []


def random_word():
    words = [
        'amarillo', 'azul', 'blanco', 'gris', 'casa', 'cielo', 'claro', 'color', 'comida', 'correr',
        'corto', 'creer', 'cruzar', 'cuadro', 'cuerpo', 'dama', 'dado', 'dulce', 'edad', 'elefante',
        'empezar', 'encontrar', 'entender', 'escalar', 'escribir', 'espacio', 'esperar', 'estrella', 'estudiar', 'feliz',
        'flor', 'frutilla', 'fruta', 'fuego', 'gato', 'girar', 'grande', 'gelatina', 'guitarra', 'hablar',
        'hacer', 'hermano', 'hijo', 'historia', 'hora', 'huevo', 'idea', 'igual', 'jugar', 'largo',
        'leer', 'libro', 'luz', 'madre', 'mano', 'mar', 'mesa', 'mirar', 'mover', 'mujer',
        'naranja', 'negro', 'nueve', 'nube', 'ojo', 'oso', 'padre', 'piso', 'palabra', 'papel',
        'parar', 'paso', 'paz', 'pozo', 'perro', 'pez', 'pie', 'piedra', 'pintar', 'plata',
        'poder', 'pollo', 'prueba', 'punto', 'querer', 'roto', 'risa', 'reloj', 'rojo', 'rosa',
        'saber', 'sal', 'saltar', 'sentir', 'ser', 'silla', 'sol', 'sonreir', 'suave', 'subir',
        'taza', 'termo', 'temprano', 'tiempo', 'tigre', 'tomar', 'toro', 'trabajar', 'tres', 'ver',
        'verde', 'viaje', 'volar', 'volver', 'zapato', 'zorro', 'abrir', 'aceite', 'agua', 'alto',
        'amigo', 'animal', 'dinosaurio', 'arena', 'bajo', 'boca', 'brazo', 'cabeza', 'calor', 'cama',
        'campo', 'carne', 'ciudad', 'clase', 'clave', 'cocina', 'comer', 'copa', 'carro', 'cuerda',
        'dormir', 'duro', 'escuela', 'familia', 'fiesta', 'flaco', 'fuerza', 'gafas', 'gente', 'gracias',
        'hambre', 'hombre', 'invierno', 'foto', 'joven', 'juego', 'lago', 'lento', 'libre', 'llave',
        'lluvia', 'luna', 'madera', 'manzana', 'mariposa', 'mes', 'mono', 'mesa', 'nadar', 'nieve',
        'nuevo', 'oro', 'pan', 'pelo', 'piedra', 'piel', 'pluma', 'puerta', 'queso', 'rata',
        'ropa', 'sopa', 'tigre', 'torta', 'vaca', 'viento', 'vino', 'vivir', 'yerba', 'zumo'
    ]
    return random.choice(words)

chosen_word = random_word()

def view_random_word(randomWord):
    for index, letter in enumerate(randomWord):
        if index < len(randomWord) - 1:
            print("-", end=" ")
        else:
            print("-", end="")

def user_selection():
    return input("Por favor, elija una letra: ").lower()

def game(letter, word, chosen_letters, won_games, lives):
    result = ""
    
    for item in word:
        if item in chosen_letters:
            result += item
            view_random_word(chosen_word)
        else:
            result += '_'
            lives -= 1
            view_random_word(chosen_word)
            # wrong_letters.append()
            # print("\n" + f"La letra elegida no está en la palabra oculta. Las siguientes son las letras incorrectas hasta el momento: {}")

    
    print(result, sep = ' ')
    

    if result == word:
        won_games += 1
        print("¡Adivinaste la palabra!", f"Partidas ganadas: {won_games}")
        return result, won_games
   
    user_guess = input("Si cree saber cuál es la palabra, escríbala a continuación o escriba 'no': ").lower()
    print(result, sep = ' ')
    if user_guess == word:
        won_games += 1
        print("¡Adivinaste la palabra!", f"Partidas ganadas: {won_games}")
        return word, won_games
    elif user_guess == 'no':
        return result, won_games
    else:
        print("Entrada no válida. Continuará el juego.")
        return result, won_games
    
welcome = lambda lives: print(f"Bienvenido al juego! Tendrás {lives} chances para adivinar la palabra oculta")

def play_game(lives):
    
    chosen_letters = []
    won_games = 0
    
    print(chosen_word)

    welcome(lives)

   

    while lives >= 1:
        view_random_word(chosen_word)
        print(f"\nVidas restantes: {lives}")
        letter = user_selection()

        if letter.isalpha():
            chosen_letters.append(letter)
            result, won_games = game(letter, chosen_word, chosen_letters, won_games, lives)

            if result == chosen_word:
                print("¡Avivinaste la palabra!", f"Partidas ganadas: {won_games}")
                break   
        else:
            print("Por favor, ingrese una letra válida.")

        

    print(f"Letras elegidas hasta ahora: {chosen_letters}")

    play_again = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    return play_again == 's'

# Juego principal
while True:
    if not play_game(lives):
        break

print("¡Gracias por jugar! Hasta la próxima.")

