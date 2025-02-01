import sys
from dataclasses import asdict

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
    
def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'

if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')
    main()
