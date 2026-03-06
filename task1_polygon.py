class Polygon:
    def area(self) -> float|None:
        pass

class Rectangle(Polygon):
    def __init__(self, width : float, height : float):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Test.

rect = Rectangle(5, 4)
print(f"Rectangle area: {rect.area()}")

