class Point:
    def __init__(self, id, x, y, value):
        self.id = id
        self.x = x
        self.y = y
        self.value = value
    
    def __str__(self):
        return f"Point {self.id} (x:{self.x}, y:{self.y}, value:{self.value})"

class Grid:
    def __init__(self):
        pass