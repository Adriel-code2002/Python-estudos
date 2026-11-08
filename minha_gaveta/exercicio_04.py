import os
while True:
   os.system('clear')
   algo = input('digite algo? ')
   print('É um numero', algo.isnumeric())

   sair = input('DESEJA ENCERRA? BOTE 00:')
   if sair == '00':
      print('um dia de cada vez🙌')
      break
