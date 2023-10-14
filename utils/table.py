from tabulate import tabulate


class TableGenerator:
    def __init__(self, moves, game_rules):
        self.moves = moves
        self.game_rules = game_rules

    def draw_matrix(self):
        """
        Function draw matrix with data of determine winner.

        :return:
        """
        table_data = [[self.game_rules.determine_winner(move1, move2) for move2 in self.moves] for move1 in self.moves]
        return table_data

    def generate_table(self):
        """
        Function generate help table.

        :return:
        """
        header = ["v PC\\User >"]
        header.extend(self.moves)
        table_data = self.draw_matrix()

        return tabulate(table_data, headers=header, tablefmt="grid")
