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

    def sum(matrixA: "Matrix", matrixB: "Matrix"):
        pass

#     __add__ → para permitir a + b

# __eq__ → para comparar objetos (==)

# __len__, __getitem__, __iter__, etc.

# _atributo → protegido (convenção)

# __atributo → privado (name mangling)

# @staticmethod: não depende de self nem cls

# @classmethod: depende da classe, não da instância

# @classmethod
# def identidade(cls, n: int) -> "Matrix":
#     m = cls(n, n)
#     for i in range(n):
#         m.matrix[i][i] = 1
#     return m


# def determinant(self) -> float:
#     """Calcula o determinante da matriz (apenas 2x2 por enquanto)."""
#     if self.rows == 2 and self.cols == 2:
#         a, b = self.matrix[0]
#         c, d = self.matrix[1]
#         return a*d - b*c
    # raise NotImplementedError


if __name__ == "__main__":
    a: Matrix = Matrix(3, 3) 
