
class Day8:
    """
    https://adventofcode.com/2022/day/8
    """

    def __init__(self):
        self.grid = []
        self.max_scenic_score = 0

    def parse(self, filename: str):
        with open(filename) as file:
            for line in file.readlines():
                row = [int(tree) for tree in line.rstrip("\n")]
                self.grid.append(row)

    def is_tree_visible(self, tree_row: int, tree_column: int) -> bool:
        tree_to_compare = self.grid[tree_row][tree_column]

        # tree is on the edge
        if tree_row == 0 or tree_column == 0 or tree_row == len(self.grid) - 1 or tree_column == len(self.grid[0]) - 1:
            return True

        # row
        if all([tree < tree_to_compare for tree in self.grid[tree_row][tree_column + 1:]]) or all(
                [tree < tree_to_compare for tree in self.grid[tree_row][:tree_column]]):
            return True

        # column
        def check_column(column: list, tree: int, tree_position: int):
            if all([i < tree for i in column[tree_position + 1:]]) or all([i < tree for i in column[:tree_position]]):
                return True
            return False

        column = []
        for row in range(len(self.grid)):
            column.append(self.grid[row][tree_column])
        return check_column(column, tree_to_compare, tree_row)

    def count_scenic_score(self, tree_row: int, tree_column: int) -> int:
        if tree_row == 0 or tree_column == 0 or tree_row == len(self.grid) - 1 or tree_column == len(self.grid[0]) - 1:
            return 0

        tree_to_compare = self.grid[tree_row][tree_column]

        def count_number_of_trees_top_the_top_and_bottom(column: list, tree_position: int) -> tuple[list, list]:
            trees_to_the_bottom = [tree for tree in column[tree_position + 1:]]
            trees_to_the_top = [tree for tree in column[:tree_position]]
            return trees_to_the_top, trees_to_the_bottom

        column = []
        for row in range(len(self.grid)):
            column.append(self.grid[row][tree_column])

        trees_to_the_top, trees_to_the_bottom = count_number_of_trees_top_the_top_and_bottom(column, tree_row)
        trees_to_the_right = [tree for tree in self.grid[tree_row][tree_column + 1:]]
        trees_to_the_left = [tree for tree in self.grid[tree_row][:tree_column]]

        def count(tree_to_compare, trees):
            result = 0
            for tree in trees:
                result += 1
                if tree >= tree_to_compare:
                    break
            return result

        right = count(tree_to_compare, trees_to_the_right)
        left = count(tree_to_compare, trees_to_the_left[::-1])
        top = count(tree_to_compare, trees_to_the_top[::-1])
        bottom = count(tree_to_compare, trees_to_the_bottom)

        return top * bottom * right * left

    def run(self, filename: str):
        self.parse(filename)
        visible_trees = 0
        for tree_row in range(len(self.grid)):
            for tree_column in range(len(self.grid[0])):
                scenic_score = self.count_scenic_score(tree_row, tree_column)
                if scenic_score > self.max_scenic_score:
                    self.max_scenic_score = scenic_score
                visible_trees += self.is_tree_visible(tree_row, tree_column)
        print(f"Number of visible trees: {visible_trees}")
        print(f"The highest scenic score is: {self.max_scenic_score}")
        return visible_trees
