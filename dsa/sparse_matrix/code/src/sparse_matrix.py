class SparseMatrix:
    def __init__(self, file_path):
        self.rows = 0
        self.cols = 0
        self.data = {}  # keys: (row, col), value: int
        self._load_from_file(file_path)

    def _load_from_file(self, file_path):
        try:
            with open(file_path, 'r') as f:
                lines = f.readlines()
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                if line.startswith("rows="):
                    self.rows = int(line.split('=')[1])
                elif line.startswith("cols="):
                    self.cols = int(line.split('=')[1])
                elif line.startswith("(") and line.endswith(")"):
                    values = line[1:-1].split(',')
                    if len(values) != 3:
                        raise ValueError("Input file has wrong format")
                    row, col, val = map(int, values)
                    self.data[(row, col)] = val
                else:
                    raise ValueError("Input file has wrong format")
        except Exception as e:
            raise ValueError("Input file has wrong format") from e

    def display(self):
        print("Sparse Matrix {}x{}".format(self.rows, self.cols))
        for key in sorted(self.data):
            print("{}: {}".format(key, self.data[key]))

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for addition")

        result = SparseMatrix.__new__(SparseMatrix)
        result.rows = self.rows
        result.cols = self.cols
        result.data = {}

        for key in self.data:
            result.data[key] = self.data[key]

        for key in other.data:
            if key in result.data:
                result.data[key] += other.data[key]
                if result.data[key] == 0:
                    del result.data[key]
            else:
                result.data[key] = other.data[key]

        return result
