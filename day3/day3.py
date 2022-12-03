
class Day3:
    """
    https://adventofcode.com/2022/day/3
    """

    @staticmethod
    def parse(filename: str):
        with open(filename) as file:
            for line in file:
                yield line.rstrip("\n")

    @staticmethod
    def priority_mapping(letter) -> int:
        letters = {
            "a": 1,
            "b": 2,
            "c": 3,
            "d": 4,
            "e": 5,
            "f": 6,
            "g": 7,
            "h": 8,
            "i": 9,
            "j": 10,
            "k": 11,
            "l": 12,
            "m": 13,
            "n": 14,
            "o": 15,
            "p": 16,
            "q": 17,
            "r": 18,
            "s": 19,
            "t": 20,
            "u": 21,
            "v": 22,
            "w": 23,
            "x": 24,
            "y": 25,
            "z": 26,
            "A": 27,
            "B": 28,
            "C": 29,
            "D": 30,
            "E": 31,
            "F": 32,
            "G": 33,
            "H": 34,
            "I": 35,
            "J": 36,
            "K": 37,
            "L": 38,
            "M": 39,
            "N": 40,
            "O": 41,
            "P": 42,
            "Q": 43,
            "R": 44,
            "S": 45,
            "T": 46,
            "U": 47,
            "V": 48,
            "W": 49,
            "X": 50,
            "Y": 51,
            "Z": 52,
        }
        return letters[letter]

    def count_items(self, rucksack) -> int:
        compartment_1 = set(rucksack[: len(rucksack) // 2])
        compartment_2 = set(rucksack[len(rucksack) // 2:])

        items_in_common = compartment_1.intersection(compartment_2)

        priorities = 0

        for item in items_in_common:
            priorities += self.priority_mapping(item)

        return priorities

    def run(self, filename: str):
        result = 0
        for rucksack in self.parse(filename):
            result += self.count_items(rucksack)
        return result


class Day3SecondStar(Day3):
    @staticmethod
    def parse(filename):
        lines = []
        with open(filename) as file:
            for line in file:
                lines.append(line.rstrip("\n"))
        return lines

    def find_badge(self, rucksack1, rucksack2, rucksack3):
        """find a common item in 3 rucksacks"""
        badge = list(
            set(rucksack1).intersection(set(rucksack2)).intersection(set(rucksack3))
        )
        return self.priority_mapping(badge[0])

    def run(self, filename: str):
        result = 0
        rucksacks = self.parse(filename)
        for i in range(0, len(rucksacks), 3):
            result += self.find_badge(rucksacks[i], rucksacks[i + 1], rucksacks[i + 2])
        return result
