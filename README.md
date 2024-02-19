# Do jogo

Projeto de jogo que eu estou fazendo para o curso de Desenvolvimento de Jogos. O jogo é um jogo de tabuleiro e a versão online é apenas para que eu possa testar com amigos onlines que ficaram interessados no projeto.

### Explicando as regras do jogo no momento:

- Os jogadores são rovers em marte que podem voltar para a casa ao completarem missões
- Ao longo do tabuleiro, existem algumas célular marcadas que quando os jogadores a alcançam, eles completam uma missão.
- Para o jogador conseguir voltar para casa, é necessário que ele alcance a base de lançamento e que tenha mais missões completadas que o último a regressar.
- Cada jogador pode se mover para um dos quatro pontos cardeais em seu turno.
- Todo jogador que conseguir regressar vence.
- O jogo termina quando o último jogador regressar ou matematicamente for impossível haver mais regressos. Quem não conseguir regressar, perde.

### Problemas conhecidos que aceito sugestões para tratá-lo.

- A depender de como as posições foram sorteadas no início, o jogo terá seu final determinado antes de começar, sendo basicamente um [jogo resolvido](https://en.wikipedia.org/wiki/Solved_game)

- Avaliar se valeria a pena que o movimento do jogador seja "King's move".

- O jogo no playtest (duas pessoas, 8x8) terminou em dois minutos. Acredito que o jogo deva ter uma duração mais prolongada.

# Provisionando

## Rodando os testes do jogo.

<code>
python -m unittest tests/test.py
</code>

## Preparando o ambiente com conda.

<pre>
conda create -n chanceler
conda activate chanceler
pip install discord.py python-dotenv
echo TOKEN=[O token do bot ] >.env
</pre>

## Ativando o bot

<pre>
conda activate chanceler
python mainbot.py
</pre>

# Você perdeu!
