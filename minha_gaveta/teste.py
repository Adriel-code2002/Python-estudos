import os
import random
# ==== FASE 1 === #
numero = random.randint(1, 50)
os.system('clear')

while True:
    palpite = int(input('qual é o seu palpite? :'))
    if palpite < numero:
       print('maior😁')

    elif palpite > numero:
       print('menor fellow😂')

    else:
       print('finalmente você acertou parabéns🙌')
       input('aperte Enter para pular para proximo jogo👑')
       break

# ==== AGORA JOGO 2 ==== #
import os
while True:
   os.system('clear')
   print('agora comeca jogo 2')
   print('===================')
   print('==adivinhe a celebridade ==')
   print()

   print('quem foi o maior rei do pop de todos os tempos?:')

   print('a) elvis presley🕺')      
   print('b) neymar jr🤾')
   print('c) michael jackson🕴️')

   escolha = input('qual das opcões e a correta:')

   if escolha == 'a':
      print('errou😂')

   elif escolha == 'b':
      print('serio o neymar? kkkk errou de novo😂')

   elif escolha == 'c':
      print('agora você acertou kkk parabens')

   sair = input('deseja encerra jogo? bote emoji 🕴️:')
   if sair == '🕴️':
      print('tchau tchau amigo🥸')
      break
   
