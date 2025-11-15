from math import sqrt, pow

class Point:
    def __init__(self, index: int, x_coordinate: float, y_coordinate: float) -> None:
        self.index: int = index
        self.x: float = x_coordinate
        self.y: float = y_coordinate

    def __str__(self) -> str:
        return f"Point #{self.index} ({self.x}, {self.y})"

# Entrada:
# Z  - 3 ≤Z ≤50000
# X1 Y1
# X2 Y2
# ...
# XZ YZ - Xi e Yi, −10^6≤Xi, Yi ≤10^6,
# indicando as coordenadas da  ́arvore i. Podem existir pontos repetidos





# Parte 2: perimetro_do_triangulo, index_arvore_1, index_arvore_2, index_arvore_3

class Grid:
    def __init__(self) -> None:
        self.points: dict[int:Point] = {}
        
    def add_point(self, index, coord_x, coord_y) -> None:
        self.points[index] = Point(index, coord_x, coord_y)
        return

    def distance(self, point_a: Point, point_b: Point) -> float:
        partial_x: float = pow(point_a.x - point_b.x, 2)
        partial_y: float = pow(point_a.y - point_b.y, 2)
        return sqrt(partial_x + partial_y)
    
    def get_minimal_perimeter(self) -> float:
        return 0.0

    
# Divisão e Conquista

# Delimitar menor perímetro possível entre 3 árvores A B C : MIN(AB), MIN(BC), MIN(CA)







