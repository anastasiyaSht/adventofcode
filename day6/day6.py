
class Day6:
    """
    https://adventofcode.com/2022/day/6
    """

    @staticmethod
    def parse(filename: str) -> str:
        with open(filename) as file:
            return file.readline()

    def subroutine(self, datastream, n):
        for letter_index in range(len(datastream)):
            packet = [datastream[letter_index + n] for n in range(n)]
            if len(set(packet)) == len(packet):
                return letter_index + n

    def run(self, filename: str, n: int):
        """n: number of unique letters sequence to find"""
        datastream_buffer = self.parse(filename)
        result = self.subroutine(datastream_buffer, n)
        return result
