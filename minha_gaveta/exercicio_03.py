import os
while True:
    os.system('clear')
    print('============================')
    print('=== EXERCICIO DE PYTHON🐍===')
    n1 = int(input('digite um valor:'))
    n2 = int(input('digite um segundo valor:'))

    s = n1 + n2

    print('a soma entre {} e {} vale {}!'.format(n1, n2, s))

    sair = input('deseja encerra? bote frase MATRIX: ')
    if sair == 'MATRIX':
       print('ate logo 🙌')
       break
       
