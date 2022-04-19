class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def count_surface_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, sideLength):
        super().__init__(sideLength, sideLength)


class Cube():
    def __init__(self, square: Square):
        self.square = square
        self.height = square.height

    def count_surface_area(self):
        return self.square.count_surface_area() * 6

    def count_volume(self):
        return self.square.count_surface_area() * self.height


class Cuboid():
    def __init__(self, figure, height):
        self.base = figure
        self.height = height

    def count_volume(self):
        return self.base.count_surface_area() * self.height

    def count_surface_area(self):
        return 2 * self.base.count_surface_area() + 2 * self.base.width * self.height + 2 * self.base.height * self.height


rectangle = Rectangle(5, 7)
print("Rectangle (w:5, h:7), surface area:", rectangle.count_surface_area())

square = Square(4)
print("Square (side:4), surface area:", square.count_surface_area())

cube = Cube(Square(4))
print("Cube (side:4), surface area:", cube.count_surface_area())
print("Cube (side:4), volume area:", cube.count_volume())

cuboid = Cuboid(Rectangle(2, 3), 4)
print("Cuboid (Rectangle [2,3], h:4), surface area:",
      cuboid.count_surface_area())
print("Cuboid (Rectangle [2,3], h:4), volume area:", cuboid.count_volume())
