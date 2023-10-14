from unittest import TestCase
from utils.rules import Rules


class TestRules(TestCase):
    def setUp(self):
        self.rules = Rules(["Rock", "Paper", "Scissors", "3rd move", "4th", "5th"])

    def test_draw(self):
        self.assertEqual(self.rules.determine_winner("Rock", "Rock"), "Draw")

    def test_win(self):
        self.assertEqual(self.rules.determine_winner("Rock", "Scissors"), "Win")

    def test_lose(self):
        self.assertEqual(self.rules.determine_winner("Paper", "Rock"), "Lose")

    def test_invalid_moves(self):
        with self.assertRaises(ValueError):
            self.rules.determine_winner("InvalidMove", "Rock")
