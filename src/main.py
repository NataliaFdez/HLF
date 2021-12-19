# IMPORT
import numpy as np
import pandas as pd
import utils
import constants


# REVANCHA

revancha = True
while revancha:
  name_user = utils.welcome()
  player = utils.User()
  pc = utils.User() 

  # random_boats()
  player_coordinates = [('A', 10)]
  pc_coordinates = [('C', 1)]

  utils.insert_boats(player_coordinates, pc_coordinates, player, pc)

  # TURNS
  play = True
  while play:
      utils.shoot_player(pc_coordinates, player, pc)
      print(f'\n{name_user} estos son tus disparos.', player.shots, f'{name_user} estos son tus barcos.', player.boats, 'PC estos son tus disparos.', pc.shots, 'PC estos son tus barcos.', pc.boats, sep = '\n\n')

      if len(player_coordinates) == 0 or len(pc_coordinates) == 0:
          break

      utils.shoot_pc(player_coordinates, pc, player)
      print(f'\n{name_user} estos son tus disparos.', player.shots, f'{name_user} estos son tus barcos.', player.boats, 'PC estos son tus disparos.', pc.shots, 'PC estos son tus barcos.', pc.boats, sep = '\n\n')

      if len(player_coordinates) == 0 or len(pc_coordinates) == 0:
          break

  # END OF GAME
  if len(player_coordinates) == 0:
    print(constants.GAME_OVER)
    pass

  if len(pc_coordinates) == 0:
        print(constants.LEVEL_UP)
                                                                 
  pass
  
  respuesta = input(f'{name_user} quieres jugar otra partida? Escribe SI ó NO.').upper()

  while respuesta != 'SI' and respuesta != 'NO':
    print(respuesta)
    print('No te he entendido')
    respuesta = input('Echamos otra partida? Escribe SI ó NO.').upper()


  if respuesta == 'SI':
    revancha = True
    player.clear()
    pc.clear()
    print('¡EMPECEMOS!')

  elif respuesta == 'NO':
    revancha = False
    print('Fin del juego')
    utils.despedida()

