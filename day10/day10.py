
class Day10:
    """
    https://adventofcode.com/2022/day/10
    """

    def __init__(self):
        self.state = 1
        self.cycle = 0
        self.result = 0
        self.crt = [[], [], [], [], [], []]

    @staticmethod
    def parse(filename: str):
        with open(filename) as file:
            for line in file:
                yield line.rstrip("\n")

    def noop_process(self):
        pass

    def addx_process(self, cycle):
        self.add_cycle()
        instruction, amount = cycle.split(" ")
        self.state += int(amount)

    def check_cycle(self):
        if self.cycle in [20, 60, 100, 140, 180, 220]:
            self.result += self.state * self.cycle
            print(self.cycle, self.state, self.state * self.cycle)

    def add_cycle(self):
        self.draw()
        self.crt[self.cycle // 40].append("#")
        self.cycle += 1
        self.check_cycle()


    def draw(self):
        if self.state == self.cycle % 40 or self.state == (self.cycle % 40) - 1 or self.state == (self.cycle % 40) + 1:
            self.crt[self.cycle // 40].append("#")
        else:
            self.crt[self.cycle // 40].append(".")


    def run(self, filename):
        for instruction in self.parse(filename):

            self.add_cycle()

            if instruction.startswith("noop"):
                self.noop_process()

            elif instruction.startswith("addx"):
                self.addx_process(instruction)

        print(self.cycle)
        for row in self.crt:
            print("".join(row))
        return self.result
