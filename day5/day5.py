import re
import typing as t


class Day5:
    """
    https://adventofcode.com/2022/day/5
    """

    def __init__(self):
        self.stacks = []

    def parse(self, filename: str):
        """Parse the blocks and moves"""
        with open(filename) as file:
            lines = file.readlines()

        number_of_stacks = self.find_stacks_number(lines)
        stacks = [[] for i in range(number_of_stacks)]
        stack_lines = self.find_stack_lines(lines)

        for line in stack_lines:
            column_number = 0
            for block in line.replace("   ", " []").split(" "):
                if block == "":
                    continue
                elif block == "[]":
                    column_number += 1
                else:
                    stacks[column_number].append(block.strip("[]"))
                    column_number += 1

        moves = self.parse_moves(lines)
        self.stacks = stacks
        return moves

    @staticmethod
    def find_stacks_number(lines: t.List[str]):
        """Finds a number of columns"""
        for line in lines:
            if line.strip().rstrip("\n").startswith("1"):
                number_of_stacks = int(line.strip().rstrip("\n")[-1])
        return number_of_stacks

    @staticmethod
    def find_stack_lines(lines: t.List[str]):
        """Saves only block lines"""
        stack_lines = []
        for line in lines:
            if line.strip().rstrip("\n").startswith("1"):
                return stack_lines
            stack_lines.append(line.rstrip("\n"))

    @staticmethod
    def parse_moves(lines: t.List[str]):
        """Saves only 'move x from y to z' lines"""
        moves = []
        for line in lines:
            if line.startswith("move"):
                moves.append(line.rstrip("\n"))
        return moves

    def make_move_single_block(self, move):
        """First star: CrateMover 9000, one block to move"""
        numbers = re.findall(r"\d+", move)

        count_of_blocks_to_move = int(numbers[0])
        start = int(numbers[1]) - 1
        destination = int(numbers[2]) - 1

        for i in range(count_of_blocks_to_move):
            block_to_move = self.stacks[start].pop(0)
            self.stacks[destination].insert(0, block_to_move)

    def make_move_multiple_blocks(self, move):
        """Second star: CrateMover 9001 can move a few blocks per one move"""
        numbers = re.findall(r"\d+", move)

        count_of_blocks_to_move = int(numbers[0])
        start = int(numbers[1]) - 1
        destination = int(numbers[2]) - 1

        blocks_to_move = self.stacks[start][:count_of_blocks_to_move]
        self.stacks[start] = self.stacks[start][count_of_blocks_to_move:]
        self.stacks[destination][:0] = blocks_to_move

    def run_first_star(self, filename: str):
        moves = self.parse(filename)
        print(self.stacks)
        for move in moves:
            self.make_move_single_block(move)

    def run_second_star(self, filename: str):
        moves = self.parse(filename)
        print(self.stacks)
        for move in moves:
            self.make_move_multiple_blocks(move)

    def print_result(self):
        result = ""
        for line in self.stacks:
            result += line[0]
        print(result)
