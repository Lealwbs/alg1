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
        
    def add_point(self, index, coord_x, coord_y) -> None:
        self.points[index] = Point(index, coord_x, coord_y)

    def distance(self, point_a: Point, point_b: Point) -> float:
        partial_x: float = pow(point_a.x - point_b.x, 2)
        partial_y: float = pow(point_a.y - point_b.y, 2)
        return sqrt(partial_x + partial_y)
    
    def get_minimal_perimeter_points(self) -> tuple:
        # compare_lexically_tuples()
        return (3, 4, 5)

    def get_minimal_perimeter(self) -> float:
        ids: tuple[int, int, int] = self.get_minimal_perimeter_points()
        point_A: Point = self.points[ids[0]] 
        point_B: Point = self.points[ids[1]] 
        point_C: Point = self.points[ids[2]] 
        # point_A = Point(997, 0, 0)
        # point_B = Point(998, 3, 0)
        # point_C = Point(999, 0, 4)
        return self.distance(point_A, point_B) + self.distance(point_B, point_C) + self.distance(point_C, point_A)
    
# Divisão e Conquista
# Delimitar menor perímetro possível entre 3 árvores A B C : MIN(AB), MIN(BC), MIN(CA)







