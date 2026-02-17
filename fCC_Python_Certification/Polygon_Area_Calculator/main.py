from abc import ABC, abstractmethod
from math import sqrt


class Rectangle(ABC):
    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height

    def set_width(self, width) -> None:
        self._width = width

    def set_height(self, height) -> None:
        self._height = height

    def get_area(self) -> int:
        return self._width * self._height

    def get_perimeter(self) -> int:
        return 2 * (self._width * self._height)

    def get_diagonal(self) -> float:
        return sqrt(self._width ** 2 + self._height ** 2)

    def get_picture(self) -> str:
        if self._width > 50 or self._height > 50:
            return 'Too big for picture.'
        picture = ''
        for h in range(self._height):
            picture += self._width * '*' + '\n'
        return picture

    def get_amount_inside(self, shape) -> int:
        return ((self._width // shape._width) *
                (self._height // shape._height))

    def __str__(self):
        return f'Rectangle({self._width=}, {self._height=})'


class Square(Rectangle):
    def __init__(self, side: int) -> None:
        super().__init__(side, side)

    def set_width(self, side: int) -> None:
        self._width = side
        self._height = side

    def set_height(self, side: int) -> None:
        self._width = side
        self._height = side
    
    def set_side(self, side: int) -> None:
        self._width = side
        self._height = side
        
    def __str__(self):
        return f'Rectangle(side={self._width})'


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
