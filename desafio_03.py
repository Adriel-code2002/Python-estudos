import os
while True: #aqui fica o loop
  os.system('clear') #essa parte é responsavel por limpar tela quando programa for iniciado
  print('=' * 20)
  print('DESAFIO 03 DE PYTHON🐍')
  n1 = int(input('digite o primeiro numero: ' ))
  n2 = int(input('digite segundo numero: ' ))
  s = n1 + n2
  print('a soma entre {} e {} vale {}!'.format(n1, n2, s)) #essa parte e responsavel pelo calculo
  
  sair = input('deseja encerra o programa? aperte 00:')
  if sair == '00': #encerramento do programa
     print('PROGRAMA ENCERRADO COM SUCESSO🐍')
     break

