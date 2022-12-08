
class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __repr__(self):
        return f"{self.name}: {self.size}"


class Directory:
    def __init__(self, name: str, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
        self.files = []
        self.size = 0

    def __repr__(self):
        return f"{self.name}: {self.size}"


class Day7:
    """
    https://adventofcode.com/2022/day/7
    """

    def __init__(self):
        self.root = Directory(name="/")
        self.current_location = self.root
        self.directories = [self.root]
        self.total_space = 70000000
        self.desired_free_space = 30000000

    @staticmethod
    def parse(filename: str):
        with open(filename) as file:
            for line in file.readlines():
                yield line.rstrip("\n")

    @staticmethod
    def process_file(command: str, parent_directory: Directory):
        """
        Creates an instance of File object, adds it to the parent directory and increases its size.
        """
        file_size, file_name = command.split(" ")
        file = File(name=file_name, size=int(file_size))
        parent_directory.files.append(file)
        return file

    def process_dir(self, command: str, parent_directory: Directory):
        dir_command, dir_name = command.split(" ")
        directory = Directory(name=dir_name, parent=parent_directory)
        parent_directory.children.append(directory)
        self.directories.append(directory)
        return directory

    def process_cd(self, command):
        command_icon, command_to_run, directory = command.split(" ")
        if directory == "..":
            self.current_location = self.current_location.parent
        elif directory == "/":
            self.current_location = self.root
        else:
            self.current_location = [dir for dir in self.current_location.children if dir.name == directory][0]

    def process_ls(self, command):
        pass

    def process_command(self, command: str):
        if command.startswith("$"):
            if "cd" in command:
                self.process_cd(command)
            elif "ls" in command:
                self.process_ls(command)
        elif command.startswith("dir"):
            self.process_dir(command, parent_directory=self.current_location)
        else:
            self.process_file(command, parent_directory=self.current_location)

    def process_directory_sizes(self):
        for directory in self.directories:
            directory.size += sum([file.size for file in directory.files])

    def process_included_sizes(self, directory):
        if not directory.children:
            return directory.size
        for child_directory in directory.children:
            directory.size += self.process_included_sizes(child_directory)
        return directory.size

    def calculate_directories(self):
        """
        Calculates a total size of directories with a size at most 100000
        """
        return sum([directory.size for directory in self.directories if directory.size <= 100000])

    def directory_to_delete(self):
        space_to_free = self.desired_free_space - (self.total_space - self.root.size)
        directory_size_to_delete = [directory.size for directory in sorted(self.directories, key = lambda x: x.size) if directory.size > space_to_free][0]
        return directory_size_to_delete

    def run(self, filename: str):
        for command in self.parse(filename):
            self.process_command(command)
        self.process_directory_sizes()
        self.process_included_sizes(self.root)
        print(f"1star: total sizes of small directories: {self.calculate_directories()}")
        print(f"2star: size of directory to delete: {self.directory_to_delete()}")
