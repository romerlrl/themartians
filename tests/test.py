from unittest import TestCase
from models.game import Game
from models.player import Player
from models.board import Board



class TestGame(TestCase):
    def setUp(self) -> None:
        self.table = [
            ["EE", "EE", "EE", "EE"],
            ["EE", "EE", "EE", "EE"],
            ["G1", "BB", "EE", "EE"]
            ]
        self.board = Board()
        self.board.init_with_matrix(self.table)
        self.G = Game("title", self.board)
        return super().setUp()

    def test_generating_board_from_matrix(self):
        B = Board()
        B.init_with_matrix(self.table)
        self.assertEqual(B.board[2][0], "G1")

    def test_generating_board_from_random(self):
        B = Board()
        B.init_by_randomness(4, 4, 4, 4)
        bz = [B.board[x][y] for x in range(4) for y in range(4)]
        #print(bz)
        #print("\n".join(["   ".join(row) for row in B.board]))
        self.assertIn("BB", bz)
        self.assertNotIn('G0', bz)

    def test_game_with_one_player(self):
        G = self.G
        x, y = 0, 2
        P1 = Player("Sand", [x, y])
        G.add_player(new_player=P1)
        G.start_game()
        self.assertEqual(G.board[x][y], "PS")
        P1.move_left()
        self.assertEqual(G.board[x][y], "EE")
        self.assertEqual(G.board[x][y-1], "PS")
        P1.move_down()
        self.assertEqual(G.board[x+1][y-1], "PS")
        v = P1.move_down()
        self.assertFalse(v)
        self.assertEqual(P1.points, 0)
        P1.move_left()
        P1.move_down()
        self.assertEqual(P1.points, 10)
        self.assertEqual(G.board[2][0], "PS")
        P1.move_up()
        self.assertEqual(G.board[2][0], "EE")
        P1.move_right()
        v = P1.move_down()
        self.assertTrue(v)
        G.print_board()
        self.assertEqual(G.board[2][1], "BB")
        self.assertTrue(all(['PS' not in row for row in G.board ]))
        self.assertFalse(P1 in G.players)

    def test_can_move(self):
        G = self.G
        G.print_board()
        G.start_game()
        self.G.board[0][1] = "P1"
        self.assertFalse(G.can_move(0, 1))
        self.assertFalse(G.can_move(-1, 0))
        self.assertFalse(G.can_move(1, -1))
        self.assertFalse(G.can_move(4, 0))
        self.assertFalse(G.can_move(1, 6))
        self.assertTrue(G.can_move(0, 0))
        self.assertTrue(G.can_move(2, 0))
        self.assertTrue(G.can_move(2, 1))

    def test_funcion_of_turn(self):
        G = self.G
        SAND  = Player("Sand", [0, 0])
        ROMER = Player("Romer",[0, 3])
        G.add_player(new_player = SAND)
        G.add_player(new_player = ROMER)
        G.start_game()
        #Falso para o Romer se move
        self.assertFalse(G.is_the_player_turn(ROMER))
        #Verdadeiro para Sand se move
        self.assertTrue(G.is_the_player_turn(SAND))
        #Executa movimento de Sand
        SAND.move_down()
        #Falso para novo movimento de Sand
        self.assertFalse(G.is_the_player_turn(SAND))
        self.assertTrue(G.is_the_player_turn(ROMER))
        #Movimento inválido de Romer
        ROMER.move_up()
        self.assertFalse(G.is_the_player_turn(SAND))
        self.assertTrue(G.is_the_player_turn(ROMER))
        ROMER.move_left()
        self.assertTrue(G.is_the_player_turn(SAND))
        self.assertFalse(G.is_the_player_turn(ROMER))
        SAND.move_down()
        ROMER.move_left()
        SAND.move_right()
        self.assertFalse(G.is_the_player_turn(SAND))
        self.assertTrue(G.is_the_player_turn(ROMER))
        ROMER.move_down()
        self.assertFalse(G.is_the_player_turn(SAND))
        self.assertTrue(G.is_the_player_turn(ROMER))
