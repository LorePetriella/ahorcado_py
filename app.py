import random

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

print(chosen_word)

input("Por favor elija una letra  ").lower()





