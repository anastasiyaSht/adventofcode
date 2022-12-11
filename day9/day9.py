
class Head:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __repr__(self):
        return f"{self.x}, {self.y}"


class Tail:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.visited_cells = {Point(self.x, self.y)}

    def __repr__(self):
        return f"{self.x}, {self.y}"


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"[{self.x}, {self.y}]"

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False


class Day9:
    """
    https://adventofcode.com/2022/day/9
    """

    def __init__(self):
        self.head = Head()
        self.tail = Tail()

    @staticmethod
    def parse(filename: str):
        with open(filename) as file:
            for line in file.readlines():
                yield line.rstrip("\n").split(" ")

    def check_head_and_tail(self, point1=None, point2=None):
        if abs(self.head.x - self.tail.x) <= 1 and abs(self.head.y - self.tail.y) <= 1:
            return True
        return False

    def is_diagonal(self, point1=None, point2=None):
        if abs(self.head.x - self.tail.x) == 2 and abs(self.head.y - self.tail.y) == 1 or\
                abs(self.head.x - self.tail.x) == 1 and abs(self.head.y - self.tail.y) == 2:
            return True
        return False

    def move_tail_diagonally(self):
        # if head is to the right top, we need to move tail to the right top
        if self.head.x - self.tail.x > 0 and self.head.y - self.tail.y > 0:
            self.tail.x += 1
            self.tail.y += 1

        # if head is to the left top, we need to move tail to the left top
        elif self.head.x - self.tail.x < 0 and self.head.y - self.tail.y > 0:
            self.tail.x -= 1
            self.tail.y += 1

        # if head is to the right bottom, we need to move tail to the right bottom
        elif self.head.x - self.tail.x > 0 and self.head.y - self.tail.y < 0:
            self.tail.x += 1
            self.tail.y -= 1

        # if head is to the left bottom, we need to move tail to the left bottom
        elif self.head.x - self.tail.x < 0 and self.head.y - self.tail.y < 0:
            self.tail.x -= 1
            self.tail.y -= 1

        self.add_tail_visited_point()

    def add_tail_visited_point(self):
        self.tail.visited_cells.add(Point(self.tail.x, self.tail.y))
        print(self.tail.visited_cells)

    def do_motion(self, direction: str, steps: int):
        print(f"DIRECTION: {direction}, STEPS: {steps}")
        for step in range(steps):
            print(f"START POSITION: [{self.head}], [{self.tail}]")
            if direction == "R":
                self.head.x += 1
                if not self.check_head_and_tail():
                    if self.is_diagonal():
                        self.move_tail_diagonally()
                    else:
                        self.tail.x += 1
                    self.add_tail_visited_point()

            elif direction == "L":
                self.head.x -= 1
                if not self.check_head_and_tail():
                    if self.is_diagonal():
                        self.move_tail_diagonally()
                    else:
                        self.tail.x -= 1
                    self.add_tail_visited_point()

            elif direction == "U":
                self.head.y += 1
                if not self.check_head_and_tail():
                    if self.is_diagonal():
                        self.move_tail_diagonally()
                    else:
                        self.tail.y += 1
                    self.add_tail_visited_point()

            elif direction == "D":
                self.head.y -= 1
                if not self.check_head_and_tail():
                    if self.is_diagonal():
                        self.move_tail_diagonally()
                    else:
                        self.tail.y -= 1
                    self.add_tail_visited_point()

    def run(self, filename: str):
        for motion in self.parse(filename):
            direction, steps = motion
            self.do_motion(direction, int(steps))
        print(f"VISITED CELLS: {len(self.tail.visited_cells)}")


class Knot:
    def __init__(self, followed_by=None):
        self.x = 0
        self.y = 0
        self.followed_by = followed_by
        self.visited_cells = {Point(self.x, self.y)}

    def __repr__(self):
        return f"{self.x}, {self.y}"


class Day9SecondStar(Day9):

    def __init__(self):
        self.knot9 = Knot()
        self.knot8 = Knot(followed_by=self.knot9)
        self.knot7 = Knot(followed_by=self.knot8)
        self.knot6 = Knot(followed_by=self.knot7)
        self.knot5 = Knot(followed_by=self.knot6)
        self.knot4 = Knot(followed_by=self.knot5)
        self.knot3 = Knot(followed_by=self.knot4)
        self.knot2 = Knot(followed_by=self.knot3)
        self.knot1 = Knot(followed_by=self.knot2)
        self.head = Knot(followed_by=self.knot1)

    def check_head_and_tail(self, point1=None, point2=None):
        if abs(point1.x - point2.x) <= 1 and\
                abs(point1.y - point2.y) <= 1:
            return True
        return False

    def is_diagonal(self, point1=None, point2=None):
        if abs(point1.x - point2.x) == 2 and abs(point1.y - point2.y) == 1 or\
                abs(point1.x - point2.x) == 1 and abs(point1.y - point2.y) == 2:
            return True
        return False

    # @staticmethod
    def add_point_visited_point(self, point):
        point.visited_cells.add(Point(point.x, point.y))
        print(self.knot9.visited_cells)

    def move_point_diagonally(self, previous_point, point):
        # if head is to the right top, we need to move tail to the right top
        if previous_point.x - point.x > 0 and previous_point.y - point.y > 0:
            point.x += 1
            point.y += 1

        # if head is to the left top, we need to move tail to the left top
        elif previous_point.x - point.x < 0 and previous_point.y - point.y > 0:
            point.x -= 1
            point.y += 1

        # if head is to the right bottom, we need to move tail to the right bottom
        elif previous_point.x - point.x > 0 and previous_point.y - point.y < 0:
            point.x += 1
            point.y -= 1

        # if head is to the left bottom, we need to move tail to the left bottom
        elif previous_point.x - point.x < 0 and previous_point.y - point.y < 0:
            point.x -= 1
            point.y -= 1

        self.add_point_visited_point(point)


    def do_motion(self, direction: str, steps: int):
        print(f"DIRECTION: {direction}, STEPS: {steps}")
        for step in range(steps):
            print(f"START POSITION: [{self.head}], [{self.knot1}], [{self.knot2}]")
            if direction == "R":
                self.head.x += 1
                point = self.head.followed_by
                while point.followed_by:
                    if not self.check_head_and_tail(self.head, self.head.followed_by):
                        if self.is_diagonal(point, point.followed_by):
                            self.move_point_diagonally(point, point.followed_by)
                        else:
                            point.x += 1
                        self.add_point_visited_point(point)
                    point = point.followed_by

            elif direction == "L":
                self.head.x -= 1
                point = self.head.followed_by
                while point.followed_by:
                    if not self.check_head_and_tail(self.head, self.head.followed_by):
                        if self.is_diagonal(point, point.followed_by):
                            self.move_point_diagonally(point, point.followed_by)
                        else:
                            point.x -= 1
                        self.add_point_visited_point(point)
                    point = point.followed_by

            elif direction == "U":
                self.head.y += 1
                point = self.head.followed_by
                while point.followed_by:
                    if not self.check_head_and_tail(self.head, self.head.followed_by):
                        if self.is_diagonal(point, point.followed_by):
                            self.move_point_diagonally(point, point.followed_by)
                        else:
                            point.y += 1
                        self.add_point_visited_point(point)
                    point = point.followed_by

            elif direction == "D":
                self.head.y -= 1
                point = self.head.followed_by
                while point.followed_by:
                    if not self.check_head_and_tail(self.head, self.head.followed_by):
                        if self.is_diagonal(point, point.followed_by):
                            self.move_point_diagonally(point, point.followed_by)
                        else:
                            point.y -= 1
                        self.add_point_visited_point(point)
                    point = point.followed_by

    def run(self, filename: str):
        for motion in self.parse(filename):
            direction, steps = motion
            self.do_motion(direction, int(steps))
        print(f"VISITED CELLS: {len(self.knot9.visited_cells)}")




