from unittest import TestCase
from tabulate import tabulate

from utils.rules import Rules
from utils.table import TableGenerator


class TestTableGenerator(TestCase):
    def setUp(self):
        self.moves = ['Rock', 'Paper', '3rd move', '4th', '5th', '6th', '7th']
        self.expected_table_data = [['Draw', 'Win', 'Win', 'Win', 'Lose', 'Lose', 'Lose'],
                                    ['Lose', 'Draw', 'Win', 'Win', 'Win', 'Lose', 'Lose'],
                                    ['Lose', 'Lose', 'Draw', 'Win', 'Win', 'Win', 'Lose'],
                                    ['Lose', 'Lose', 'Lose', 'Draw', 'Win', 'Win', 'Win'],
                                    ['Win', 'Lose', 'Lose', 'Lose', 'Draw', 'Win', 'Win'],
                                    ['Win', 'Win', 'Lose', 'Lose', 'Lose', 'Draw', 'Win'],
                                    ['Win', 'Win', 'Win', 'Lose', 'Lose', 'Lose', 'Draw']]
        self.game_rules = Rules(self.moves)
        self.table_generator = TableGenerator(self.moves, self.game_rules)

    def test_draw_matrix(self):
        result = self.table_generator.draw_matrix()
        self.assertEqual(result, self.expected_table_data)

    def test_generate_table(self):
        expected_table = tabulate(self.expected_table_data,
                                  headers=["v PC\\User >"] + self.moves,
                                  tablefmt="grid")
        result = self.table_generator.generate_table()
        self.assertEqual(result, expected_table)
