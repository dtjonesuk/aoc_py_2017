import io
import os


class Input():
    def __init__(self, input_path: str = "input.txt", from_string:str|None=None, strip_lines:bool = True, strip_empty:bool=True):
        self.input_path = input_path
        self.from_string = from_string
        self.strip_empty = strip_empty
        self.strip_lines = strip_lines

    def open(self):
        if self.from_string is not None:
            f = io.StringIO(self.from_string)
            return f
        else:
            # filename
            return open(self.input_path, "r")

    def read_lines(self):
        with self.open() as f:
            lines = [line.strip() if self.strip_lines else line.rstrip(os.linesep) for line in f.readlines()]
            if self.strip_empty:
                lines = [line for line in lines if len(line) > 0]
        return lines

    def read_lines_as_chars(self):
        return [list(line) for line in self.read_lines()]

    def read_lines_as_ints(self):
        lines = self.read_lines()
        return [int(line) for line in lines]

    def read_lines_as_tsv(self):
        lines = self.read_lines()
        return [[value.strip() for value in line.split()] for line in lines]

    def read_lines_as_tsv_ints(self):
        lines = self.read_lines_as_tsv()
        return [[int(value) for value in line] for line in lines]

    def read_lines_as_csv(self):
        lines = self.read_lines()
        return [[value.strip() for value in line.split(',')] for line in lines]

    def read_lines_as_csv_ints(self):
        lines = self.read_lines_as_csv()
        return [[int(value) for value in line] for line in lines]


