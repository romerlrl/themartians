import discord
from discord.ext import commands
from dotenv import dotenv_values
from discord.member import Member
from models.game import Game
from models.board import Board
from models.player import Player
# Crie uma instância do bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)  # Defina o prefixo do comando (use o que preferir)
B = Board()
B.init_by_randomness()
LG = Game("O Jogo", B)
all_players = []
all_players_dict = {}
emojis = ["blue_circle",  "brown_circle",  "green_circle",  "orange_circle", "purple_cicle", "red_circle", "yellow_circle"]
# Comando para inicializar uma partida
@bot.command()
async def start(ctx, player1: Member = None, player2: Member = None, player3: Member = None, player4: Member = None, player5: Member = None, player6: Member = None, player7: Member = None):
    params = [player1, player2, player3, player4, player5, player6, player7]
    send_ = ""
    i = 0
    for player in params:
        if isinstance(player, Member) and player not in all_players_dict:
            P = LG.add_player(f"{i}{player.name}")
            all_players.append(P)
            all_players_dict[player] = P
            send_+=f"{player.mention} - "
            i+=1
    LG.start_game()
    LG.print_board()

    await ctx.send(f"Partida inicializada! Jogarão {send_[:-2:]}, \n {show_table()}")

# Comando para jogar
@bot.command()
async def jogar(ctx, message ):
    print(ctx)
    P = all_players_dict.get(ctx.author, None)
    if P is None:
        return
    if message.lower() in {"l", "left", "<", "a", "esq", "esquerda"}:
        v = P.move_left()
    if message.lower() in {"r", "right", ">", "d", "dir", "direita"}:
        v = P.move_right()
    if message.lower() in {"u", "up", "^", "w", "cima"}:
        v = P.move_up()
    if message.lower() in {   "down", "s", "baixo", "para baixo", "pra baixo"}:
        v = P.move_down()
    if not v:
        await ctx.send("Espere sua vez")

        return
    table = show_table()
    await ctx.send(table)


def show_table():
    table = ""
    for key, value in all_players_dict.items():
        table+=f"{key.name}: {value.points} \t"
    for x in range(len(LG.board)):
        table+='\n'
        for y in range(len(LG.board[x])):
            ch, n = LG.board[x][y]

            if ch == "E":
                table+=f":{'black' if x%2 == y%2 else 'white'}_medium_square:"
            elif ch == "B":
                table+=f":rocket:"
            elif ch == "G":
                table+=":large_orange_diamond:"
            elif ch == "P":
                table+=f":{emojis[int(n)]}:"

    return table





@bot.command()
async def close(ctx):
    exit()

# Evento quando o bot estiver pronto
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user.name} ({bot.user.id})")

# Execute o bot com o token do seu bot

bot.run(dotenv_values(".env")["TOKEN"])
