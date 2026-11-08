import os
while True:
   os.system('clear')
   a = input('digite algo jovem:')
   print('O tipo primitivo e ',type(a))
   print('so tem espaços?', a.isspace())
   print(' E um numero?', a.isnumeric())
   print('É alfabetico',a.isalpha())
   print('Està em maiuscula?',a.isupper())
   print('Està em minuscula?',a.islower())
   print('Esta capitalizada?',a.istitle())

   sair = input('pra encerra programa, digite DEUS: ')
   if sair == 'DEUS':
      print('programa encerrado🐍')
      break
