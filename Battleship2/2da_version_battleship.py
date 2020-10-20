import random
from time import sleep

# Definir tablero, donde se mostrará estacios en blanco (representando agua),
# y x (representando barcos)


tablero_usuario = [
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
]

tablero_pc = [
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
]

# Se define tablero donde se representarán los disparos ejecutados por el usuario (sean acertados o fallidos)
intentos_usuario = [
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
]

intentos_pc = [
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
]

# Para poder definir el tablero 10x10 con coodenadas alfanumericas, se definió un diccionario 
# Lo anterior debido a que Python accede a las listas por número, 
# De aqui e adelante tomaremos en cuenta que las listas en python comienzan en 0 no en 1

letras_a_numeros = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5, 
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9
}


# Empezamos a definir funciones que podremos llamar al código más adelante y asi resumimos la sintaxis

#Definimos la posición de los barcos del jugador 
def preguntar_posicion_barcos_usuario():
    columna = input("Escribe una sola letra que esté dentro de este rango para definir la columna (ABCDEFGHIJ):").upper()
    while columna not in "ABCDEFGHIJ":
        print("Columna incorrecta! Debería  estar dentro del rango: ABCDEFGHIJ")
        columna = input("Escribe una sola letra que esté dentro de este rango para definir la columna (ABCDEFGHIJ):")

    fila = int(input("Escribe un solo numero dentro de este rango para definir la fila (1 al 10):"))
    while fila not in [1,2,3,4,5,6,7,8,9,10]:
        print("Fila incorrecta! Debería ser del 1 al 10")
        fila = int(input("Escribe un solo numero dentro de este rango para definir la fila (1 al 10):"))

    # El código que llama a esta funcion recibirá los valores enumerados en la declaración de retorno 
    # estos pueden ser asignados a variables
    # A fila se le resta 1, ya que anteriormente comentamos que pythn comienza a leer los numeros desde 0
    # En la variable letras a números, inertamos una letra pero python nos regresará un número, segun el diccionario,
    # Con lo anterior se puede colocar en el tablero de 10x10
    return int(fila) - 1, letras_a_numeros[columna]


def imprimir_tablero_consola(tablero):
    # Mostraremos el tablero del usuario, una fila a la vez
    print("   A B C D E F G H I J")
    print("  +-+-+-+-+-+-+-+-+-+-+")
    fila_numero = 1
    for fila in tablero:
        if fila_numero == len(tablero):
            print("%d|%s|" % (fila_numero, "|".join(fila)))
        else:
            print("%d |%s|" % (fila_numero, "|".join(fila)))
        print("  +-+-+-+-+-+-+-+-+-+-+")
        fila_numero = fila_numero + 1

# Función que nos ayuda a registrar nuevos barcos usuario
def eleccion_usuario():
    print("En dónde quieres colocar tu barco ", n + 1, "?")
    fila_numero, columna_numero = preguntar_posicion_barcos_usuario()

    # Revisar que las posiciones de los barcos nos e repitan
    if tablero_usuario[fila_numero][columna_numero] == 'X':
        print("Ya existe un barco ahí!")
        eleccion_usuario()
    else:
        tablero_usuario[fila_numero][columna_numero] = 'X'
        imprimir_tablero_consola(tablero_usuario)

def pregunta_posicion_barcos_pc():
    columna = random.randint(1,10)
    fila = random.randint(1,10)
    return int(fila) - 1, int(columna) - 1

# Función que nos ayuda a registrar nuevos barcos pc
def eleccion_pc():
    fila_numero, columna_numero = pregunta_posicion_barcos_pc()
    # Revisar que las posiciones no se repitan
    if tablero_pc[fila_numero][columna_numero] == 'X':
        eleccion_pc()
    else:
        tablero_pc[fila_numero][columna_numero] = 'X'


# Ahora comenzamos con los disparos del usuario, esto será hasta que los disparos coincidan con los barcos de pc

disparos_usuario = 0
disparos_pc = 0

def turno_disparos_juego_usuario():
    print("Adivina la posición de un barco")
    fila_numero, columna_numero = preguntar_posicion_barcos_usuario()

    if intentos_usuario[fila_numero][columna_numero] != ' ':
        print("Ya habías disparado en esas coordenadas,inténtalo de nuevo novato!")
        turno_disparos_juego_usuario()

    # Checamos que los disparos no se repitan
    if tablero_pc[fila_numero][columna_numero] == 'X':
        print("Acertaste! sigue así, golpear primero, gorpear fuerte, sin piedad")
        intentos_usuario[fila_numero][columna_numero] = 'X'
        disparos_usuario = disparos_usuario + 1
    else:
        intentos_usuario[fila_numero][columna_numero] = '.'
        print("fuck, que pésimo eres")

    print("Estos son los disparos que llevas:")
    imprimir_tablero_consola(intentos_usuario)

def turno_disparos_juego_pc():
    print('SKYNET disparó')
    fila_numero, columna_numero = pregunta_posicion_barcos_pc()

    if intentos_pc[fila_numero][columna_numero] != ' ':
        turno_disparos_juego_pc()

    # Checamos que los disparos no se repitan
    if tablero_usuario[fila_numero][columna_numero] == 'X':
        print('BOOM, la SKYNET acertó')
        intentos_pc[fila_numero][columna_numero] = 'X'
        disparos_pc = disparos_pc + 1
    else:
        intentos_pc[fila_numero][columna_numero] = '.'
        print('FIU, la SKYNET falló')
        

    print('Estos son los disparos de SKYNET:')
    imprimir_tablero_consola(intentos_pc)




#
# Aqui terinmos de escribir las funciones que necesitamos para correr el juego
# Runtime
# Comenzamos a codificar el storytelling del juego
#
print('Bienvenido a BATTLESHIP 3.0, si estás listo para poner a prueba tus habilidades como gamer, atrevete a jugar.')
print('COMENCEMOS!')
print('1.Tendrás que elegir la posición de 3 barcos, capturando una letra y un número, esta posicion se verá reflejada en un tablero de 10x10, y así lo haras de forma consecutiva hasta tener la posición de tus 3 barcos en el tablero.')
print('2.De forma automática, tu contrincante "SKYNET" elegirá la posicion de sus barcos.') 
print('3.Comenzarás a capturar tus disparos para el hundiemiento de la flota de SKYNET')
print('¡SUERTE NOVATO!')                                 
        
inicio = input('Quieres comenzar? Para iniciar, escribe yes (y) para aceptar el reto o una (n) si decides retirarte:').upper()


if inicio in ['Y']:
    # Registro de barcos para pc o para jugador

    for i in range(3):
        eleccion_pc()
    #Aqui sólo comprobamos que se estuviera creando el tablero de la pc de forma correcta, pero este se oculta
    print('Este es el tablero de SKYNET:')
    imprimir_tablero_consola(tablero_pc)

    # Como solo debemos de tener 3 barcos, se usa un loop for para pedir un barco solo 3 veces
    print('Es tu turno de ubicar tus naves.')
    for n in range(3):
        eleccion_usuario()

else: 
    # Si el usuario responde que no quiere jugar, damos una despedida
    print('Vaya, se que regresarás pronto a intentarlo')
    exit()

# Si el jugador decide coemnzar a jugar , damos saltos de linea para que se limpie la pantalla en consola
# aumentamos salto de línea 150

print("\n"*50)

disparos_usuario = 0
disparos_pc = 0
contador_turnos = 0

while disparos_pc < 3 or disparos_usuario < 3 or contador_turnos < 20:
    turno_disparos_juego_usuario() 
    print("\n"*10)   
    sleep(5)
    turno_disparos_juego_pc()
    print("\n"*10) 
    sleep(5)
    contador_turnos = contador_turnos + 1


if turno_disparos_juego_usuario == 3:
    print('GANASTE! el sr miyagi estaría orgulloso de ti')    

else:
    if turno_disparos_juego_pc == 3:
        print('LOSER! nadie puede contra las máquinas')   
    
    if contador_turnos == 20:
        print('No pudiste derrotar a SKYNET en pocos turnos, vete de aqui!')

    
# Al momento de completar 3==x, es decir hundir los 3 barcos, se cierra el ciclo
# imprimimos la salida del juego
print("GAME OVER!")




