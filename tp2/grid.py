from math import sqrt, pow

class Point:
    def __init__(self, index: int, x_coordinate: float, y_coordinate: float) -> None:
        self.index: int = index
        self.x: float = x_coordinate
        self.y: float = y_coordinate

    def __str__(self) -> str:
        return f"Point #{self.index} ({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return f"Point #{self.index} ({self.x}, {self.y})"


class Grid:
    def __init__(self) -> None:
        self.points: dict[int:Point] = {}
        self.px: list[int] = [] # ID dos pontos ordenados pelo eixo X
        self.py: list[int] = [] # ID dos pontos ordenados pelo eixo Y

    def __str__(self) -> str:
        result: str = f"Grid ({len(self.points)} points):\n"
        for point in self.points.values():
            result += f"{point}\n"
        return result

    # Printa os pontos de um dicionário ou lista para debug
    def print_points(self, struct: dict | list ) -> None:
        result: str = ""
        if type(struct) == dict: 
            for i in struct:
                result += f"{i}: {struct[i]}\n"
        if type(struct) == list:
            for i in struct:
                if type(i) == int:
                    result += f"{i}: {self.points[i]}\n"
                else:
                    result += f"{i[0]}: {i[1]}\n"
        print(result)
        
    def add_point(self, index, coord_x, coord_y) -> None:
        self.points[index] = Point(index, coord_x, coord_y)

    def min_lexically(self, tuple_a: tuple[int, int, int], tuple_b: tuple[int, int, int]) -> tuple:
        for i in range(3):
            if tuple_a[i] < tuple_b[i]: return tuple_a
            if tuple_a[i] > tuple_b[i]: return tuple_b
        return tuple_a

    def distance(self, point_a: Point, point_b: Point) -> float:
        partial_x: float = pow(point_a.x - point_b.x, 2)
        partial_y: float = pow(point_a.y - point_b.y, 2)
        return sqrt(partial_x + partial_y)
    
    def perimeter(self, id_a, id_b, id_c) -> float:
        if not (id_a or id_b or id_c): return 0
        point_A: Point = self.points[id_a] 
        point_B: Point = self.points[id_b] 
        point_C: Point = self.points[id_c] 
        return self.distance(point_A, point_B) + self.distance(point_B, point_C) + self.distance(point_C, point_A)
    
    def sort_points(self) -> None:
        self.px = sorted(self.points.keys(), key=lambda index: self.points[index].x)
        self.py = sorted(self.points.keys(), key=lambda index: self.points[index].y)
    
    def get_minimal_perimeter_points(self) -> tuple:
        self.sort_points()
        return self.divide_conquer(self.px, self.py)
    
    def divide_conquer(self, px_range: list[int], py_range: list[int]) -> tuple:
        n = len(px_range)
        
        # Caso base: força bruta para poucos pontos
        if n <= 10:
            return self.brute_force_triplet(px_range)
        
        # Dividir ao meio e montar os parâmetros para a recursão
        mid_index: int = n // 2
        mid_point_id: int = px_range[mid_index]
        mid_x: float = self.points[mid_point_id].x
        
        px_left = px_range[:mid_index]
        px_right = px_range[mid_index:]
        py_left = [idx for idx in py_range if self.points[idx].x <= mid_x]
        py_right = [idx for idx in py_range if self.points[idx].x > mid_x]

        triplet_left: tuple[int, int, int] = self.divide_conquer(px_left, py_left)
        triplet_right: tuple[int, int, int] = self.divide_conquer(px_right, py_right)
        
        # Escolher o melhor dos dois lados
        perim_left: float = self.perimeter(*triplet_left)
        perim_right: float = self.perimeter(*triplet_right)
        
        # Define qual tripla é melhor considerando empates (usa ordem lexicográfica)
        if perim_left < perim_right:
            best_triplet = triplet_left
            best_perimeter = perim_left
        elif perim_right < perim_left:
            best_triplet = triplet_right
            best_perimeter = perim_right
        else:
            best_triplet = self.min_lexically(triplet_left, triplet_right)
            best_perimeter = perim_left
        
        # Combina, verifica triângulos que cruzam a linha divisória (podem ser menores)
        # A faixa considera apenas pontos próximos à linha divisória (distância < melhor perímetro)
        strip = [idx for idx in py_range if abs(self.points[idx].x - mid_x) < best_perimeter]
        strip_triplet = self.find_strip_triplet(strip, best_perimeter)
        
        if strip_triplet:
            strip_perim = self.perimeter(*strip_triplet)
            if strip_perim < best_perimeter:
                return strip_triplet
            elif strip_perim == best_perimeter:
                return self.min_lexically(best_triplet, strip_triplet)
        
        return best_triplet
    
    def brute_force_triplet(self, point_ids: list[int]) -> tuple:
        n = len(point_ids)
        min_perim = float('inf')
        best_triplet = (0, 0, 0)

        if n < 3: 
            return best_triplet
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    id_a, id_b, id_c = point_ids[i], point_ids[j], point_ids[k]
                    perim = self.perimeter(id_a, id_b, id_c)
                    
                    if perim < min_perim:
                        min_perim = perim
                        best_triplet = tuple(sorted([id_a, id_b, id_c]))
                    elif perim == min_perim:
                        candidate = tuple(sorted([id_a, id_b, id_c]))
                        best_triplet = self.min_lexically(best_triplet, candidate)
        
        return best_triplet
    
    def find_strip_triplet(self, strip: list[int], current_min: float) -> tuple:
        n = len(strip)
        if n < 3:
            return None
        
        min_perim = current_min
        best_triplet = None
        
        # Verifica apenas pontos próximos na faixa (strip já está ordenado por Y)
        for i in range(n):
            j = i + 1
            # Para cada ponto i, verifica pontos j próximos em Y (dentro do perímetro mínimo)
            while j < n and (self.points[strip[j]].y - self.points[strip[i]].y) < min_perim:
                k = j + 1
                # Para cada par (i,j), verifica pontos k também próximos em Y
                while k < n and (self.points[strip[k]].y - self.points[strip[i]].y) < min_perim:
                    id_a, id_b, id_c = strip[i], strip[j], strip[k]
                    perim = self.perimeter(id_a, id_b, id_c)
                    
                    # Atualiza o melhor triângulo encontrado na faixa
                    if perim < min_perim:
                        min_perim = perim
                        best_triplet = tuple(sorted([id_a, id_b, id_c]))
                    elif perim == min_perim and best_triplet:
                        candidate = tuple(sorted([id_a, id_b, id_c]))
                        best_triplet = self.min_lexically(best_triplet, candidate)
                    
                    k += 1
                j += 1
        
        return best_triplet