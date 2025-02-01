from dataclasses import dataclass, field, InitVar


@dataclass
class Point:
    x: int
    y: int

    __x: InitVar[int] = field(repr=False, init=False, compare=False, metadata=None)
    __y: InitVar[int] = field(repr=False, init=False, compare=False, metadata=None)


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    def post_init(self):
        self.__x = self.x
        self.__y = self.y

