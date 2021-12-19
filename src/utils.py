import numpy as np
import pandas as pd
import time
import sys
import constants

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



# BUILDING USERS

class User:
    def __init__(self):
        self.boats = pd.DataFrame('',
                                  columns = list('ABCDEFGHIJ'),
                                  index = list(range(1, 11)),
                                 )
        
        self.shots = self.boats.copy()

        return None
    
    def clear(self):
        self.boats.loc[:, :] = ''
        self.shots.loc[:, :] = ''



# random_boats()



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