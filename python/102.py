from helpers import pt, st


class LinearFunc:
    _point1 = None
    _point2 = None
    _zero_value = None
    _incr = None

    def __init__(self, point1, point2):
        self._point1 = point1
        self._point2 = point2
        self.calculate()

    def calculate(self):
        diff_x = self._point1.x - self._point2.x
        diff_y = self._point1.y - self._point2.y

        self._incr = diff_y / diff_x
        self._zero_value = self._point2.y - (self._point2.x * self._incr)

    def above_x_axis(self):
        return self._zero_value > 0

    def below_x_axis(self):
        return self._zero_value < 0

    def left_of_y_axis(self):
        return self._incr > 0 and self._zero_value > 0 \
            or self._incr < 0 and self._zero_value < 0

    def right_of_y_axis(self):
        return self._incr > 0 and self._zero_value < 0 \
            or self._incr < 0 and self._zero_value > 0


class Point:
    _x = None
    _y = None

    def __init__(self, coords):
        self._x = coords[0]
        self._y = coords[1]

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def is_left(self):
        return self._x < 0

    def is_right(self):
        return self._x > 0

    def is_top(self):
        return self._y > 0

    def is_bottom(self):
        return self._y < 0

    def __repr__(self):
        return f'[{self._x}, {self._y}]'


class Triangle:
    _coords = None
    _points = None

    def __init__(self, coords):
        self._coords = coords

    @property
    def points(self):
        if self._points is not None:
            return self._points

        self._points = [
            Point(self._coords[:2]),
            Point(self._coords[2:4]),
            Point(self._coords[4:6])
        ]
        return self._points

    def left_points(self):
        return [point for point in self.points if point.is_left()]

    def right_points(self):
        return [point for point in self.points if point.is_right()]

    def top_points(self):
        return [point for point in self.points if point.is_top()]

    def bottom_points(self):
        return [point for point in self.points if point.is_bottom()]

    def goes_above(self):
        for point_left in self.left_points():
            for point_right in self.right_points():
                linear_func = LinearFunc(point_left, point_right)
                if linear_func.above_x_axis():
                    return True

        for point in self.points:
            if point.x == 0 and point.y > 0 and self.left_points() and self.right_points():
                return True

        return False

    def goes_below(self):
        for point_left in self.left_points():
            for point_right in self.right_points():
                linear_func = LinearFunc(point_left, point_right)
                if linear_func.below_x_axis():
                    return True

        for point in self.points:
            if point.x == 0 and point.y < 0 and self.left_points() and self.right_points():
                return True

        return False

    def goes_left(self):
        for point_top in self.top_points():
            for point_bottom in self.bottom_points():
                linear_func = LinearFunc(point_top, point_bottom)
                if linear_func.left_of_y_axis():
                    return True

        for point in self.points:
            if point.y == 0 and point.x < 0 and self.top_points() and self.bottom_points():
                return True

        return False

    def goes_right(self):
        for point_top in self.top_points():
            for point_bottom in self.bottom_points():
                linear_func = LinearFunc(point_top, point_bottom)
                if linear_func.right_of_y_axis():
                    return True

        for point in self.points:
            if point.y == 0 and point.x > 0 and self.top_points() and self.bottom_points():
                return True

        return False

    def goes_around(self):
        return self.goes_above() and self.goes_below() and self.goes_left() and self.goes_left()

    def explain(self):
        return {
            'goes_around': self.goes_around(),
            'goes_left': self.goes_left(),
            'goes_right': self.goes_right(),
            'goes_above': self.goes_above(),
            'goes_below': self.goes_below()

        }

    def __repr__(self):
        return f'Triangle({self.points})'


def parse_file():
    triangles = []
    with open('files/102_triangles.txt', 'r') as base_exp_data:
        for line in base_exp_data:
            triangles.append(Triangle([int(x) for x in line[:-1].split(',')]))
    return triangles


correct = 0
triangles = parse_file()
st()
for triangle in triangles:
    if triangle.goes_around():
        # print(f'{triangle} matches')
        correct += 1
    else:
        # print(f'{triangle} doesn\'t go around')
        pass
pt()
print(correct)
