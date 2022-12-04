import typing as t


class Day4:
    """
    https://adventofcode.com/2022/day/4
    """

    @staticmethod
    def parse(filename: str):
        with open(filename) as file:
            for line in file:
                yield line.rstrip("\n").split(",")

    @staticmethod
    def get_assignment_sections(pairs: t.List[str]):
        x1, y1 = pairs[0].split("-")
        x2, y2 = pairs[1].split("-")

        assignments1 = {x for x in range(int(x1), int(y1) + 1)}
        assignments2 = {x for x in range(int(x2), int(y2) + 1)}

        return assignments1, assignments2

    def compare_pairs(self, pairs: t.List[str]) -> int:
        assignments1, assignments2 = self.get_assignment_sections(pairs)

        if assignments1.intersection(assignments2) == assignments1 \
                or assignments1.intersection(assignments2) == assignments2:
            return 1
        return 0

    def run(self, filename):
        result = 0
        for pairs in self.parse(filename):
            result += self.compare_pairs(pairs)
        return result


class Day4SecondStar(Day4):

    def compare_pairs(self, pairs: t.List[str]) -> int:
        assignments1, assignments2 = self.get_assignment_sections(pairs)

        if assignments1.intersection(assignments2):
            return 1
        return 0
