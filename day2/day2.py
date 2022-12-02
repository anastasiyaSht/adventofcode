
class Day2:
    """
    https://adventofcode.com/2022/day/2
    """

    @staticmethod
    def parse(filename: str) -> tuple:
        with open(filename) as file:
            for line in file:
                yield tuple(line.rstrip("\n").split(" "))

    @staticmethod
    def _mapping_score(choice: str) -> int:
        score = {
            "rock": 1,
            "paper": 2,
            "scissors": 3
        }
        return score[choice]

    @staticmethod
    def _mapping_letters(letter: str) -> str:
        mapping = {
            "A": "rock",
            "B": "paper",
            "C": "scissors",
            "X": "rock",
            "Y": "paper",
            "Z": "scissors"
        }
        return mapping[letter]

    @staticmethod
    def _mapping_to_win(opponent_choice: str) -> str:
        """
        Returns what beats the opponent_choice
        """
        mapping = {
            "rock": "paper",
            "paper": "scissors",
            "scissors": "rock"
        }
        return mapping[opponent_choice]

    def round(self, opponent_choice: str, your_choice: str) -> int:
        score = 0

        opponent_choice = self._mapping_letters(opponent_choice)
        your_choice = self._mapping_letters(your_choice)

        if opponent_choice == your_choice:  # if draw
            score = 3
        elif self._mapping_to_win(opponent_choice) == your_choice:  # if you win
            score = 6

        score += self._mapping_score(your_choice)
        return score

    def run(self, filename: str):
        score = 0
        for i in self.parse(filename):
            score += self.round(i[0], i[1])
        return score


class Day2SecondStar(Day2):

    @staticmethod
    def _outcome_score(letter: str) -> int:
        mapping = {
            "X": 0,
            "Y": 3,
            "Z": 6
        }
        return mapping[letter]

    @staticmethod
    def _mapping_outcome(letter: str) -> str:
        mapping = {
            "X": "lose",
            "Y": "draw",
            "Z": "win"
        }
        return mapping[letter]

    @staticmethod
    def _mapping_result(opponent_choice: str, outcome: str) -> str:
        """
        Returns what you need to choose depending on the result of the round
        """
        mapping = {
            "lose": {
                "rock": "scissors",
                "paper": "rock",
                "scissors": "paper"
            },
            "draw": {
                "rock": "rock",
                "paper": "paper",
                "scissors": "scissors"
            },
            "win": {
                "rock": "paper",
                "paper": "scissors",
                "scissors": "rock"
            }
        }
        return mapping[outcome][opponent_choice]

    def round(self, opponent_choice: str, outcome: str) -> int:
        score = 0

        score += self._outcome_score(outcome)
        score += self._mapping_score(
            choice=self._mapping_result(opponent_choice=self._mapping_letters(opponent_choice),
                                        outcome=self._mapping_outcome(outcome))
        )
        return score
