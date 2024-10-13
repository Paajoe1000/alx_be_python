class Shape:
    def area(self) -> float:
        raise NotImplementedError  ("Sunclasses should implement this!")
    
class Rectangle(Shape):
    def __init__(self, lenght: float, width: float) -> None:
        self.length = lenght
        self.width = width

    def area(self) -> float:
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self) -> float:
        import math
        return math.pi * (self.radius ** 2)
