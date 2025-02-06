
from math import radians, sin
from dataclasses import dataclass
from io import StringIO

@dataclass
class Parallelogram:
    side1: float
    side2: float
    angle: float

    """
    def __init__(self, side1 = 0, side2 = 0, angle = 0):
        self.side1 = side1
        self.side2 = side2
        self.angle = angle
    """

    def get_area(self) -> float:
        return sin(radians(self.angle)) * self.side1 * self.side2

    def get_perimeter(self) -> float:
        return 2 * (self.side1 + self.side2)


    def __repr__(self) -> str:
        return f'Parallelogram {{ side1={self.side1}, side2={self.side2}, angle={self.angle} }}'


    def __str__(self) ->str:
        retval = StringIO() # roughly similar to Java and C# StringBuilder class
        retval.write('( ')
        retval.write(f'side1={self.side1}, side2={self.side2}, angle={self.angle}')
        retval.write(' )')
        return retval.getvalue()