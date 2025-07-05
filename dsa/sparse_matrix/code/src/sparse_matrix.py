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

            # First line: matrix dimensions (e.g., 4 4)
            dims = lines[0].strip().split()
            if len(dims) != 2:
                raise ValueError("Invalid matrix size line. Expected 'rows cols'.")

            self.rows = int(dims[0])
            self.cols = int(dims[1])

            # Remaining lines: non-zero values in format "row col value"
            for line in lines[1:]:
                parts = line.strip().split()
                if len(parts) != 3:
                    continue  # Skip invalid lines
                row, col, val = map(int, parts)
                if val != 0:
                    self.data[(row, col)] = val

        except Exception as e:
            raise ValueError("Input file has wrong format") from e

    def display(self):
        print(f"Sparse Matrix {self.rows}x{self.cols}")
        for key in sorted(self.data):
            print(f"{key}: {self.data[key]}")

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
