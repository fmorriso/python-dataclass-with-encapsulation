from dataclasses import asdict

from point import Point


def main():
    p1 = Point(2, 4)
    print(p1)
    print(asdict(p1))

if __name__ == '__main__':
    main()
