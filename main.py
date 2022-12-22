from play_functions.play_functions import muda_jogador, render_jogo, entra_coluna, jogar, reset_jogo
from victory_tests.victory_tests import testa_vitoria

jogo = []
jogador = ['\033[31mO\033[m',]
reset_jogo(jogo)
print(f'PRÓXIMO JOGADOR: {jogador[0]}')
while True:
  render_jogo(jogo)
  coluna = entra_coluna(jogo)
  jogar(coluna, jogo, jogador)
  if testa_vitoria(jogo, jogador):
    break
  muda_jogador(jogador)
  print(f'PRÓXIMO JOGADOR: {jogador[0]}')

render_jogo(jogo)
print(f'VITÓRIOA DE {jogador[0]}')
