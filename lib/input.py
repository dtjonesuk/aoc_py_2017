import io

class Input():
    def __init__(self, input_path: str = "input.txt", from_string:str|None=None, strip_empty:bool=True):
        self.input_path = input_path
        self.from_string = from_string
        self.strip_empty = strip_empty

    def open(self):
        if self.from_string is not None:
            f = io.StringIO(self.from_string)
            return f
        else:
            # filename
            return open(self.input_path, "r")

    def read_lines(self):
        with self.open() as f:
            lines = [line.strip() for line in f.readlines()]
            if self.strip_empty:
                lines = [line.strip() for line in lines if len(line.strip()) > 0]
        return lines

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


