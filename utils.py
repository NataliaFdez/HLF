import numpy as np
import pandas as pd
import time
import sys
import constants
import string



# WELCOME

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)

def welcome():
    delay_print('\n - ¡BIENVENIDO AL HUNDIR LA FLOTA! - \n')
    print(constants.BARCO_BIENVENIDA)

    delay_print('Ring! Ring!\n')
    delay_print('¿Diga? ¿Con quién hablo?\n')
    name_user = input()
    delay_print(f'¡Con que tu eres {name_user}! ¡Te estaba esperando! ¡Yo soy tu mayor enemigo! ¡¡Muajajaja!! Te reto a una partida de hundir la flota.\n')
    delay_print('bip... bip... bip... \n')
    delay_print('Movilizando a la armada.\n')
    delay_print('.......................\n')
    delay_print('Desplegando la flota.   \n')
    delay_print('.......................\n')
    delay_print(f'¡Preparate {name_user}! ¡Esto es la guerra! ')
    delay_print('¡Al ataque!')
    return name_user

# BUILDING OCEAN

def ocean_dimension():
    
    while True:
        try:
            size = int(input('\n\nIntroduce el tamaño del lado del tablero que quieras usar (en número):'))
            break
        except ValueError: 
            continue

    if size <= 0:
        print('¿Un océano de antimateria? Mejor juguemos con el tablero clásico de 10x10...')
        size = 10
        col_index = list(string.ascii_uppercase)[:size] 

    elif size < 10:
        print('¿Eso es un océano o un embalse? Mejor juguemos con el tablero clásico de 10x10...')
        size = 10
        col_index = list(string.ascii_uppercase)[:size]

    elif size <= 26:
        col_index = list(string.ascii_uppercase)[:size] 

    elif 26 < size <= 676:
        duoble_alphabet = list(itertools.product(string.ascii_uppercase,
            repeat = 2))
        col_index = list(string.ascii_uppercase) + [(str(letters[0]) + str(letters[1])) for letters in duoble_alphabet]
    
    elif size <= 19000:
        triple_alphabet = list(itertools.product(string.ascii_uppercase,
            repeat = 3))
        col_index = list(string.ascii_uppercase) + [(str(letters[0]) + str(letters[1]) + str(letters[2])) for letters in triple_alphabet]
    
    elif size > 19000:
        print('''
            Según Wikipedia:
            Océano
            Cuerpo de agua
            Superficie:          361 000 000 km²
            Volumen:           1 300 000 000 km³
            Profundidad Media:         3 900 m
    
            Si cada casilla equivale a 1km², has
            creado un tablero más grande que toda
            la lámina de agua del planeta.
    
            Si te lo estabas preguntando, Challenger Deep
            está en la casilla 11°22.4′N 142°35.5′E.
            
            Mejor juguemos con el tablero clásico de 10x10...
        ''')
        size = 10
        col_index = list(string.ascii_uppercase)[:size] 
    
    ocean = (size + 1, col_index)
    
    return ocean



# BUILDING USERS

class User:
    def __init__(self):
        self.boats = pd.DataFrame('',
                                  columns = list('ABCDEFGHIJ'),
                                  index = list(range(1, 11)),
                                 )
        
        self.shots = self.boats.copy()

        return None
    
    def boats_generator(self, fleet, ocean):
        coordinates = []
        fleet.sort(reverse = True)

        for ship in fleet:
            boat_in = False
            attemps = 0
            
            if attemps == 100:
                print('Uno de los barcos se ha averiado y no ha podido desplegarse.')
            
            while boat_in == False:
                bow = np.random.randint(0, ocean[0])
                course = ocean[1].index(np.random.choice(ocean[1]))
                way = np.random.choice(list('NSEW'))
                
                if way == 'N' or way == 'E':
                    stern = bow + ship
                    way = 1
                    zone = self.boats.iloc[bow: stern: way, course]

                    # Check if zone inside ocean:
                    condition_1 = bow in range(self.shots.shape[0])
                    condition_2 = stern in range(self.shots.shape[0])
                    
                    # Check if zone is empty:
                    condition_3 = True
                    for element in zone:
                        if element != '': condition_3 = False
                    
                    if condition_1 and condition_2 and condition_3:
                        self.boats.iloc[bow: stern: way, course] = 'O'
                        boat_in = True

                    else:
                        attemps +=1
                        continue
                    
                if way == 'S' or way == 'W':
                    stern = bow - ship
                    way = -1
                    zone = self.boats.iloc[course, bow: stern: way]
                    
                    # Check if zone inside ocean:
                    condition_1 = bow in range(self.shots.shape[0])
                    condition_2 = stern in range(self.shots.shape[0])
                    
                    # Check if zone is empty:
                    condition_3 = True
                    for element in zone:
                        if element != '': condition_3 = False
                    
                    if condition_1 and condition_2 and condition_3:
                        self.boats.iloc[bow: stern: way, course] = 'O'
                        boat_in = True

                    else:
                        attemps +=1
                        continue
                        
        for row in range(self.boats.shape[0]):
            for col in range(self.boats.shape[1]):
                if self.boats.iloc[row, col] == 'O':
                    coordinates.append((ocean[1][col], row + 1))
                    
        return coordinates
    
    def clear(self):
        self.boats.loc[:, :] = ''
        self.shots.loc[:, :] = ''



# GENERATE FLEET

def fleet():
        fleet = input('\n\nIntroduce la flota con la que vamos a jugar y pulsa ENTER:\n' + 
                    'Deberás introducir la eslora de cada barco, separada por comas.\n' +
                    '\nPor ejemplo: 1,1,1,1,2,2,2,3,3,4 creará:\n\n' +
                    'Cuatro barcos de eslora 1\n' +
                    'Tres barcos de eslora 2\n' +
                    'Dos barcos de eslora 3\n' +
                    'Un barco de eslora 4\n')

        fleet = fleet.strip().replace(' ', '').split(sep = ',')
        fleet = list(map(int, fleet))

        return fleet



# INSERT BOATS

def insert_boats(player_coordinates, pc_coordinates, player, pc):
    for i in player_coordinates:
        player.boats.loc[i[1],i[0]] = "O"

    for i in pc_coordinates:
        pc.boats.loc[i[1],i[0]] = '0'



# SHOOT

def shoot_player(pc_coordinates, player, pc):
    raw_coord = input('Introduce coordenadas:').upper()
    row = int(raw_coord[1:])
    col = raw_coord[0]
    coordinates = pc_coordinates
    
    # Comprobar si las coordenadas se salen del tablero
    while (row > 11 or row < 1) or (col not in list('ABCDEFGHIJ')):
        print('Coordenadas erróneas.')
        raw_coord = input('Introduce coordenadas:').upper()
        row = int(raw_coord[1:])
        col = raw_coord[0]
    
    # Comprobar si ya se ha disparado anteriormente a esa coordenada
    while (player.shots.loc[row, col] != ''):
        print('Ya has disparado a ese lugar.')
        raw_coord = input('Introduce coordenadas:').upper()
        row = int(raw_coord[1:])
        col = raw_coord[0]
    
    # Pintar X si se ha acertado y ~ si se ha fallado
    if ((col, row)) in coordinates:
        coordinates.remove((col, row))
        player.shots.loc[row, col] = 'X'
        pc.boats.loc[row, col] = 'X'
        
    else:
        player.shots.loc[row, col] = '~'
        pc.boats.loc[row, col] = '~'


def shoot_pc(player_coordinates, pc, player):
    row = np.random.randint(11)
    col = np.random.choice(list('ABCDEFGHIJ'))
    coordinates = player_coordinates
    
    # Comprobar si ya se ha disparado anteriormente a esa coordenada
    while (pc.shots.loc[row, col] != ''):
        row = np.random.randint(11)
        col = np.random.choice(list('ABCDEFGHIJ'))
    
    # Pintar X si se ha acertado y ~ si se ha fallado
    if pc.shots.loc[row, col] == 'O':
        coordinates.remove((col, row))
        pc.shots.loc[row, col] = 'X'
        player.boats.loc[row, col] = 'X'
        
    else:
        pc.shots.loc[row, col] = '~'
        player.boats.loc[row, col] = '~'



# DESPEDIDA
def despedida():
    print(constants.CREDITOS)