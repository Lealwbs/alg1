class Matrix:
    def __init__(self, rows: int, cols: int):
        self.rows: int = rows
        self.cols: int = cols
        self.matrix = [ [''*cols] * rows ]
    

    def __str__(self):
        result: str = f"Matrix({self.rows} x {self.cols}):\n"
        for cols in self.rows:
            result += cols
        return result

    def sum(matrixA: Matrix, matrixB: Matrix):
        pass


