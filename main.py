import random

print ('!Juego de piedra, papel o tigeras¡')
option = ('piedra', 'papel', 'tijera')


# Contadores 
computer_wins = 0
user_wins = 0
rounds = 1

# Ciclo de juego 
while True:
  print('-'*10)
  print('ROUND', rounds)
  print('-'*10)
  user_option = input('piedra,\n papel\n tigera \n elije una opcion: ')
# Marcador 
  print(f'''Computer Wins * {computer_wins} ** {user_wins} * User Wins''')
# Opciones elejidas por el usuario y la maquina
  user_option = user_option.lower()
  rounds += 1
  if not user_option in option:
    print('Ta uste pendejo o ke mi parce!!!')
    continue
  computer_option = random.choice(option)
# Impreción de la selección  
  print(f'Tú seleccionaste => {user_option}')
  print(f'La maquina selecciono => {computer_option}')
# Ciclo if del juego para ganar, perder o empatar 
  if user_option == computer_option:
    print('Empate... sigue intentando')
  elif user_option == 'piedra':
    if computer_option == 'papel':
      print('Envuelto como tamalito; la maquina gana')
      computer_wins += 1
    else:
      print('Le rompiste las tijeras; tú ganas')
      user_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print ('Ganaste cortandolo de forma definitiva')
      user_wins += 1
    else:
      print ('Jajajaja perdiste por una roca')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'tijera':
      print('Te cortaron en trozitos como en Ecatepec')
      computer_wins += 1
    else:
      print('Ganas tú y tú y solamente tú y tú y tú...')
      user_wins += 1
  
# Ciclo de finalizacion del juego con un break 
  if computer_wins == 2:
    print('La computadora es la gran vencedora')
    break

  if user_wins == 2:
    print('No pudo contra tu nivel de IQ 100')
    break
    
  