from math import sqrt, pow

class Point:
    def __init__(self, index: int, x_coordinate: float, y_coordinate: float) -> None:
        self.index: int = index
        self.x: float = x_coordinate
        self.y: float = y_coordinate

    def __str__(self) -> str:
        return f"Point #{self.index} ({self.x}, {self.y})"


def compare_lexically_tuples(tuple_a) -> tuple:
    return tuple_a

class Grid:
    def __init__(self) -> None:
        self.points: dict[int:Point] = {}

    def __str__(self) -> str:
        result: str = f"Grid ({len(self.points)} points):\n"
        for point in self.points.values():
            result += f"{point}\n"
        return result
        
    def add_point(self, index, coord_x, coord_y) -> None:
        self.points[index] = Point(index, coord_x, coord_y)

    def distance(self, point_a: Point, point_b: Point) -> float:
        partial_x: float = pow(point_a.x - point_b.x, 2)
        partial_y: float = pow(point_a.y - point_b.y, 2)
        return sqrt(partial_x + partial_y)
    
    def get_minimal_perimeter_points(self) -> tuple:
        # compare_lexically_tuples()
        return (1, 2, 3)
    


    def get_perimeter(self, id_a, id_b, id_c) -> float:
        point_A: Point = self.points[id_a] 
        point_B: Point = self.points[id_b] 
        point_C: Point = self.points[id_c] 
        return self.distance(point_A, point_B) + self.distance(point_B, point_C) + self.distance(point_C, point_A)
    
# Divisão e Conquista
# Delimitar menor perímetro possível entre 3 árvores A B C : MIN(AB), MIN(BC), MIN(CA)







