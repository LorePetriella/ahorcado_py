import random


lives = 10
wrong_letters = []
chosen_letters = []



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

welcome = lambda lives: print(f"Bienvenido al juego! Tendrás {lives} chances para adivinar la palabra oculta")

def print_random_word(word, chosen_letters):
    for letter in word:
        if letter in chosen_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

def user_selection():
    return input("Por favor, elija una letra: ").lower()


def game(letter, word, won_games, lives, chosen_letters):
    result = ""

    if letter not in word:   
            wrong_letters.append(letter)
            print("\n" + f"La letra elegida no está en la palabra oculta. Las siguientes son las letras incorrectas hasta el momento: {wrong_letters}")
            lives -= 1
            print(f"Vidas restantes: {lives}")

    if lives == 0:
            print(f"¡Perdiste! La palabra correcta era '{word}'.")
            return word, won_games
    
    for item in word:
        
        if item in chosen_letters:
            result += item
        
        else:
            result += '_'
            
            

    
    print(result, sep = ' ')
    

    if result == word:
        won_games += 1
        print("¡Adivinaste la palabra!", f"Partidas ganadas: {won_games}")
        return result, won_games
   
    user_guess = input("Si cree saber cuál es la palabra, escríbala a continuación o escriba 'no': ").lower()
    # print(result, sep = ' ')
    

    if user_guess == word:
        won_games += 1
        print("¡Adivinaste la palabra!", f"Partidas ganadas: {won_games}")
        return word, won_games
    elif user_guess == 'no':
        return result, won_games
    else:
        print("Entrada no válida. Continuará el juego.")
        return result, won_games



    
    


def play_game(lives):
    won_games = 0
    chosen_word = random_word()
    
    chosen_letters = []
    result = "-" * len(chosen_word)  # Inicializa result con guiones
    
    welcome(lives)
    print_random_word(chosen_word, chosen_letters)
    
#   
    
    print(chosen_word)

#    
#     view_random_word(chosen_word)
    while lives >= 1 and result != chosen_word:
        print(f"\nVidas restantes: {lives}")
        print(f"Letras elegidas hasta ahora: {chosen_letters}")
        letter = user_selection()

        if letter.isalpha():
            chosen_letters.append(letter)
            result, won_games = game(letter, chosen_word, won_games, lives, chosen_letters)

        else:
            print("Por favor, ingrese una letra válida.")

    play_again = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    return play_again == 's'    
   

# Juego principal
while True:
    if not play_game(lives):
        break

print("¡Gracias por jugar! Hasta la próxima.")









 

   


