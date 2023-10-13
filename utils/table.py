from tabulate import tabulate


class TableGenerator:
    def __init__(self, moves, game_rules):
        self.moves = moves
        self.game_rules = game_rules

    def draw_matrix(self):
        table_data = []
        for move1 in self.moves:
            row = [move1]
            for move2 in self.moves:
                result = self.game_rules.determine_winner(move1, move2)
                row.append(result)

            table_data.append(row)
        return table_data

    def generate_table(self):
        """
        Function generate help table.

        :return:
        """
        header = ["v PC\\User >"]
        header.extend(self.moves)
        table_data = self.draw_matrix()

        table = tabulate(table_data, headers=header, tablefmt="grid")

        return table

