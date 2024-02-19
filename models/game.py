from models.player import Player
from models.board import Board

class Game:
    EMPTY    = 'EE'
    GOAL     = 'G'
    ACHIEVED = 'A'
    PLAYER   = 'P'
    BASE     = "BB"

    def __init__(self, title: str, board: Board):
        self.title = title
        self.board = board.board
        self.empty = board.empty_cells
        self.game_has_started = False
        self.minimal_to_raise = 0
        self.highscore = []
        self.players = []
        self.turn = 0

    def add_player(self, name: str = "", new_player: Player = None):
        if self.game_has_started:
            return
        if new_player is None:
            x, y = self.empty.pop()
            new_player = Player(name, [x, y])
        else:
            x, y = new_player.pos
        new_player.game = self
        self.board[x][y] = f"P{new_player.name[0]}"
        self.players.append(new_player)
        return new_player

    def start_game(self):
        self.game_has_started = True

    def print_board(self):
        print(f"== {self.title} ({self.turn}) ==")
        for row in self.board:
            print(" ".join(row))
        print("="*11, "\n")

    def is_the_player_turn(self, player: 'Player'):
        return self.players[self.turn % len(self.players)] == player

    def can_move(self, new_x: int, new_y: int):
        return ((0<= new_x<len(self.board)) and
                (0<=new_y<len(self.board[0])) and
                not self.board[new_x][new_y].startswith(self.PLAYER) and
                self.game_has_started
                )

    def move(self, player: 'Player', x: int, y: int):
        if not self.is_the_player_turn(player):
            return False

        new_x, new_y = player.pos[0] + x, player.pos[1] + y
        old_x, old_y = player.pos
        if self.can_move(new_x, new_y) and self.is_the_player_turn(player):
            cell = self.board[new_x][new_y]
            if cell == "BB":
                r = self.into_return_to_home(player, x, y)
                print("UEPA", r)
                if r:
                    self.board[old_x][old_y] = "EE"
                return r

            elif cell.startswith("G"):
                self.into_goal(player, x, y)
            self.board[old_x][old_y] = "EE"
            self.board[new_x][new_y] = f"P{player.name[0]}"
            self.turn = self.turn+1
            return True
        return False


    def into_return_to_home(self, player: 'Player', x: int, y: int):
        if player.points > self.minimal_to_raise:
            self.minimal_to_raise = player.points
            self.highscore.append((player, player.points))
            player.fly()
            self.players.remove(player)
            return True
        return False

    def into_goal(self, player: 'Player', x: int, y: int):
        player.points+=10
        return True

    def end_game(self):
        return