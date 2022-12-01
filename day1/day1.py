
class Day1:
    """
    https://adventofcode.com/2022/day/1
    """

    @staticmethod
    def parse(filename):
        with open(filename) as file:
            calories_per_elf = []
            for item_calories in file:
                try:
                    calories_per_elf.append(int(item_calories.rstrip("\n")))
                except ValueError:
                    yield calories_per_elf
                    calories_per_elf = []
            yield calories_per_elf

    def run_first_star(self, filename):
        max_calories_amount = 0
        for calories_per_elf in self.parse(filename):
            if sum(calories_per_elf) > max_calories_amount:
                max_calories_amount = sum(calories_per_elf)
        return max_calories_amount

    def run_second_star(self, filename):
        top_three_elves = []
        for calories_per_elf in self.parse(filename):
            # save first three elves
            if len(top_three_elves) < 3:
                top_three_elves.append(sum(calories_per_elf))
            elif any(sum(calories_per_elf) > j for j in top_three_elves):
                # replace the smallest calories amount with a bigger one
                top_three_elves[top_three_elves.index(min(top_three_elves))] = sum(calories_per_elf)
        return sum(top_three_elves)
