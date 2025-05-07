import unittest
from src.task_06 import NoSuchStrategyError, rps_game_winner, WrongNumberOfPlayersError


class TestRPS(unittest.TestCase):
    def test(self):

        # Check player validation
        with self.assertRaises(WrongNumberOfPlayersError):
            rps_game_winner(
                [["player1", "P"], ["player2", "S"], ["player3", "S"]])

        # Check startegy validation
        with self.assertRaises(NoSuchStrategyError):
            rps_game_winner([["player1", "P"], ["player2", "A"]])

        # Check p2 win
        self.assertEqual(
            rps_game_winner([["player1", "P"], ["player2", "S"]]), "player2 S"
        )

        # Check p1 win
        self.assertEqual(
            rps_game_winner([["player1", "P"], ["player2", "R"]]), "player1 P"
        )

        # Check p1 win when strategies is equal
        self.assertEqual(
            rps_game_winner([["player1", "P"], ["player2", "P"]]), "player1 P"
        )


if __name__ == "__main__":
    unittest.main()
