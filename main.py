import sys
from dataclasses import asdict

from parallelogram import Parallelogram
from point import Point


def main():
    p1 = Point(2, 4)
    print(f'{p1 = }')
    print(f'{asdict(p1) = }')

    p2 = Point(2, 4)
    print(f'{p2 = }')
    print(f'{asdict(p2) = }')

    # check equivalence and identity of the two sample instances
    print(f'{p1 == p2 = }')
    print(f'{p1 is p2 = }')

    p3 = Point()
    print(f'{p3 = }')
    print(f'{asdict(p3) = }')

    p1 = Parallelogram(2, 1, 30)
    print(p1.get_area())
    print(p1)

    p2 = Parallelogram(1, 2, 30)
    print(p2.get_area())
    print(p2) # uses __str__
    print(p2)
    
def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'

if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')
    main()
