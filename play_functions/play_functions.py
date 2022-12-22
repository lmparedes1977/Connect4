def muda_jogador(jogador):
  jg = jogador
  if jg[0] == '\033[31mO\033[m':
    jg[0] = '\033[33mO\033[m'
  else:
    jg[0] = '\033[31mO\033[m'


def render_jogo(jogo):
  jg = jogo
  print(' 1 2 3 4 5 6 7')
  for linha in jg:
    print('\033[34m|\033[m', end='')
    for coluna in linha:
      print(f'{coluna}', end='\033[34m|\033[m')
    print()


def reset_jogo(jogo):
  jg = jogo
  for i in range(6):
    linha = []
    for j in range(7):
      linha.append(' ')
    jg.append(linha)


def jogar(coluna, jogo, jogador):
  jg = jogo
  jgr = jogador
  for i in range(5, -1, -1):
    if jg[i][coluna] == ' ':
      jg[i][coluna] = jgr[0]
      break


def entra_coluna(jogo):
  jg = jogo
  while True:
    try:
      coluna = int(input("DIGITE O NÚMERO DA COLUNA: ")) - 1
      while (coluna < 0) or (coluna > 6) or (jg[0][coluna] != ' '):
        coluna = int(input("COLUNA INEXISTENTE OU CHEIA. DIGITE O NÚMERO DA COLUNA: ")) - 1
      break;
    except:
      print('ENTRADA INVÁLIDA. ENTRE COM O NÚMERO DA COLUNA:')
  return coluna

