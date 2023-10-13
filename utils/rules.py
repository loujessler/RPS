class Rules:
    def __init__(self, moves):
        self.moves = moves
        self.half = len(moves) // 2

    def determine_winner(self, move1, move2):
        """
        Function determine who is winner pc or user.

        :param move1:
        :param move2:
        :return:
        """
        if move1 == move2:
            return "Draw"

        move1_index = self.moves.index(move1)
        move2_index = self.moves.index(move2)

        if (move1_index < move2_index and move2_index - move1_index <= self.half) or (
                move1_index > move2_index and move1_index - move2_index > self.half):
            return "Win"
        else:
            return "Lose"
