#from models.game import Game
class Player:
    def __init__(self, name, pos):
        self.name   = name
        self.pos    = pos
        self.points = 0

    def _move(self, x: int, y: int):
        if self.game.move(self, x, y):
            self.pos[0]+=x
            self.pos[1]+=y
            return True
        return False

    def move_up(self):
        return self._move(-1, 0)

    def move_down(self):
        return self._move(1, 0)

    def move_left(self):
        return self._move(0, -1)

    def move_right(self):
        return self._move(0, 1)

    def fly(self, *args, **kwargs):
        return