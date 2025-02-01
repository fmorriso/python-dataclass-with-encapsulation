from dataclasses import dataclass, field, InitVar


@dataclass
class Point:
    x: int
    y: int

    # shadow the public properties with pseudo-private variables
    # that do not clutter up the class by unnecessarily participating in
    # repr, str and compare and do not appear during asdict() calls.
    __x: InitVar[int] = field(repr=False, init=False, compare=False, metadata=None)
    __y: InitVar[int] = field(repr=False, init=False, compare=False, metadata=None)


    @property
    def x(self):
        '''All references to the x attribute will be redirected to the pseudo-private shadow attributes'''
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
        '''copy the constructor values into the pseudo-private shadow attributes.'''
        self.__x = self.x
        self.__y = self.y

