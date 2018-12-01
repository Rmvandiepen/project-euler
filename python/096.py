import sys

from helpers import st, pt


class Location:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        if not isinstance(other, Location):
            raise NotImplemented(f'Cannot subtract {type(other)} from Location')

        return Location(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        if not isinstance(other, Location):
            raise NotImplemented(f'Cannot subtract {type(other)} from Location')
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.x + self.y * 10

    def __repr__(self):
        return f'Location({self.x, self.y})'


class InvalidSudokuException(Exception):
    pass


class Cell:
    location = None
    _value = None
    _available_values = None
    grid = None
    row = None
    column = None
    block = None

    def __init__(self, location):
        self.location = location
        self._available_values = list(range(1, 10))

    def get_value(self):
        return self._value

    def set_value(self, value):
        if self.is_solved():
            if self._value != value:
                raise InvalidSudokuException('Trying to set to a different value as already set')
            return

        self._value = value

        if self.grid.simulation:
            self.grid.simulation_values[self.location] = value

        self._available_values = []

        if not self.row.verify() or not self.column.verify() or not self.block.verify():
            raise InvalidSudokuException()

        self.row.remove_available_value(value)
        self.row.try_solving_all_numbers()

        self.column.remove_available_value(value)
        self.column.try_solving_all_numbers()

        self.block.remove_available_value(value)
        self.block.try_solving_all_numbers()

    def is_solved(self):
        return self._value is not None

    def remove_available_value(self, value):
        if value not in self._available_values or self.is_solved():
            return

        self._available_values.remove(value)

        if self.grid.initializing_simulation:
            return

        available_values_amount = len(self._available_values)
        if available_values_amount == 1:
            self.set_value(self._available_values[0])

        if available_values_amount in (2, 3, 4):
            self.row.try_matching_available_values(self._available_values, self)
            self.column.try_matching_available_values(self._available_values, self)
            self.block.try_matching_available_values(self._available_values, self)

        if available_values_amount == 2 and not self.grid.simulation:
            simulation_results = []
            for available_value in self._available_values:
                grid = Grid()
                grid.start_simulation(self.grid)
                try:
                    grid.get_cell(self.location).set_value(available_value)
                except InvalidSudokuException:
                    pass

                simulation_results.append(grid.simulation_values)

            if len(simulation_results) == available_values_amount:
                equal_numbers = {}
                for location, solved_value in simulation_results[0].items():
                    equal_number = True
                    for simulation_result in simulation_results:
                        if location not in simulation_result or simulation_result[location] != solved_value:
                            equal_number = False

                    if equal_number:
                        equal_numbers[location] = solved_value
                for location, value in equal_numbers.items():
                    self.grid.get_cell(location).set_value(value)

        self.row.try_to_solve_number(value)
        self.column.try_to_solve_number(value)
        self.block.try_to_solve_number(value)

    def is_value_available(self, value):
        return value in self._available_values

    def has_same_posibilities(self, other_cell):
        return self._available_values == other_cell._available_values

    def __repr__(self):
        return f'Cell(value={self._value})'

    def __str__(self):
        return self.__repr__()


class CellGroup:
    cells = None
    grid = None
    _available_values = None

    def __init__(self, cells):
        self._available_values = list(range(1, 10))

        self.cells = {}
        for x, cell in enumerate(cells):
            self.cells[x + 1] = cell

    def is_solved(self):
        for cell in self.cells.values():
            if not cell.is_solved():
                return False
        return True

    def remove_available_value(self, value):
        if value not in self._available_values:
            return

        self._available_values.remove(value)

        for cell in self.cells.values():
            cell.remove_available_value(value)

    def try_solving_all_numbers(self):
        for number in range(1, 10):
            self.try_to_solve_number(number)

    def try_to_solve_number(self, number):
        allowed_spots = []
        for location, cell in self.cells.items():
            if cell.get_value() == number:
                return

            if cell.is_value_available(number):
                allowed_spots.append(location)

        if len(allowed_spots) == 1:
            self.cells[allowed_spots[0]].set_value(number)
        elif len(allowed_spots) <= 3:
            self.use_advanced_algorithm(allowed_spots, number)

    def use_advanced_algorithm(self, allowed_spots, number):
        print('Not implemented')
        raise NotImplemented()

    def try_matching_available_values(self, available_values, from_cell):
        matching_cells = []
        for cell in self.cells.values():
            if cell.has_same_posibilities(from_cell):
                matching_cells.append(cell)
        if len(matching_cells) == len(available_values):
            for cell in self.cells.values():
                if cell not in matching_cells:
                    for number in available_values:
                        cell.remove_available_value(number)

    def verify(self):
        solved_values = []
        for cell in self.cells.values():
            if cell.is_solved():
                if cell.get_value() in solved_values:
                    return False
                solved_values.append(cell.get_value())
        return True


class Row(CellGroup):
    y = None

    def __init__(self, y, cells):
        self.y = y
        super().__init__(cells)
        for cell in self.cells.values():
            cell.row = self

    def use_advanced_algorithm(self, allowed_spots, number):
        cells_available = [self.cells[allowed_spot] for allowed_spot in allowed_spots]
        blocks_used = set([cell.block for cell in cells_available])
        if len(blocks_used) == 1:
            block = blocks_used.pop()
            for cell in block.cells.values():
                if cell not in cells_available:
                    cell.remove_available_value(number)


class Column(CellGroup):
    x = None

    def __init__(self, x, cells):
        self.x = x
        super().__init__(cells)
        for cell in self.cells.values():
            cell.column = self

    def use_advanced_algorithm(self, allowed_spots, number):
        cells_available = [self.cells[allowed_spot] for allowed_spot in allowed_spots]
        blocks_used = set([cell.block for cell in cells_available])
        if len(blocks_used) == 1:
            block = blocks_used.pop()
            for cell in block.cells.values():
                if cell not in cells_available:
                    cell.remove_available_value(number)


class Block(CellGroup):
    location = None

    def __init__(self, location, cells):
        self.location = location
        self._available_values = list(range(1, 10))

        self.cells = {}
        for location, cell in cells.items():
            self.cells[location] = cell
            cell.block = self

    def use_advanced_algorithm(self, allowed_spots, number):
        cells_available = [self.cells[allowed_spot] for allowed_spot in allowed_spots]
        rows_used = set([cell.row for cell in cells_available])
        if len(rows_used) == 1:
            row = rows_used.pop()
            for cell in row.cells.values():
                if cell not in cells_available:
                    cell.remove_available_value(number)
        columns_used = set([cell.column for cell in cells_available])
        if len(columns_used) == 1:
            column = columns_used.pop()
            for cell in column.cells.values():
                if cell not in cells_available:
                    cell.remove_available_value(number)
        pass

    def pretty_format(self):
        result = '+-------+\n'
        for y in range(1, 4):
            result += '|'
            for x in range(1, 4):
                value = self.cells[Location(x, y)].get_value()
                result += ' ' + (str(value) if value is not None else '.')
            result += ' |\n'
        result += '+-------+'
        return result

    def pretty_format_possibilities(self):
        result = '+-------+-------+-------+'
        for i in range(1, 10):
            y = int((i - 1) / 3 + 1)
            result += '\n|'
            for j in range(1, 10):
                x = int((j - 1) / 3) + 1
                cell = self.cells[Location(x, y)]
                value = cell.get_value()
                if value is not None:
                    if j - ((x - 1) * 3) == 2 and i - ((y - 1) * 3) == 2:
                        result += ' ' + str(value)
                    else:
                        result += '  '
                else:
                    number = (((i - (y-1)*3) - 1) * 3) + (j - ((x - 1) * 3))
                    if number in cell._available_values:
                        result += ' ' + str(number)
                    else:
                        result += ' .'
                if j % 3 == 0:
                    result += ' |'
            if i % 3 == 0:
                result += '\n+-------+-------+-------+'
        return result


class Grid:
    rows = None
    columns = None
    blocks = None
    cells = None
    simulation = None
    simulation_values = None
    initializing_simulation = None

    def __init__(self):
        self.cells = {}
        for x in list(range(1, 10)):
            for y in list(range(1, 10)):
                location = Location(x, y)
                cell = Cell(location)
                cell.grid = self
                self.cells[location] = cell

        self.rows = {}
        for y in list(range(1, 10)):
            row = Row(y, [cell for location, cell in self.cells.items() if location.y == y])
            row.grid = self
            self.rows[y] = row

        self.columns = {}
        for x in list(range(1, 10)):
            column = Column(x, [cell for location, cell in self.cells.items() if location.x == x])
            column.grid = self
            self.columns[x] = column

        self.blocks = {}
        for y in list(range(1, 4)):
            for x in list(range(1, 4)):
                location = Location(x, y)
                block = Block(location, {
                    Location((loc.x - 1) % 3 + 1, (loc.y - 1) % 3 + 1): cell for loc, cell in self.cells.items() if
                int((loc.x - 1) / 3) + 1 == location.x and int((loc.y - 1) / 3) + 1 == location.y
                })
                block.grid = self
                self.blocks[location] = block

    def start_simulation(self, base_grid):
        self.initializing_simulation = True
        for location, cell in base_grid.cells.items():
            value = cell.get_value()
            if value is not None:
                self.cells[location].set_value(value)
        self.initializing_simulation = False

        self.simulation = True
        self.simulation_values = {}

    def get_cell(self, location):
        return self.cells[location]

    def is_solved(self):
        for cell in self.cells.values():
            if not cell.is_solved():
                return False

        return self.verify()

    def __repr__(self):
        result = ''
        for y in list(range(1, 10)):
            for x in list(range(1, 10)):
                result += str(self.get_cell(Location(x, y))) + ', '
            result += '\n'
        return result

    def pretty_format(self):
        result = '+-------+-------+-------+'
        for y in range(1, 10):
            result += '\n|'
            for x in range(1, 10):
                value = self.get_cell(Location(x, y)).get_value()
                result += ' ' + (str(value) if value is not None else '.')
                if x % 3 == 0:
                    result += ' |'
            if y % 3 == 0:
                result += '\n+-------+-------+-------+'
        return result

    def pretty_format_possibilities(self):
        result = ''
        for y in range(1, 4):
            block_results = []
            for x in range(1, 4):
                block_results.append(self.blocks[Location(x, y)].pretty_format_possibilities().split('\n'))
            for i in range(0, len(block_results[0])):
                result += block_results[0][i] + ' ' + block_results[1][i] + ' ' + block_results[2][i] + '\n'
        return result

    def verify(self):
        for row in self.rows.values():
            if not row.verify():
                return False

        for column in self.columns.values():
            if not column.verify():
                return False

        for block in self.blocks.values():
            if not block.verify():
                return False
        return True


def parse_file():
    sudokus = []
    current = None
    y = None
    with open('files/096_sudoku.txt', 'r') as sudoku_data:
        for line in sudoku_data:
            if line[:4] == 'Grid':
                if current is not None:
                    sudokus.append(current)

                current = []
                y = 1
                continue

            for i, number in enumerate(line):
                x = i + 1
                if number in '123456789':
                    current.append((Location(x, y), int(number)))
            y += 1

        if current is not None:
            sudokus.append(current)

    return sudokus

st()
sudokus = parse_file()
print(len(sudokus))
sum = 0

for sudoku in sudokus:
    grid = Grid()
    for location, value in sudoku:
        try:
            grid.get_cell(location).set_value(value)
        except InvalidSudokuException as e:
            print('Invalid sudoku')
            break

    if not grid.is_solved():
        print('not solved')
        print(grid.pretty_format())
        # break
        # print(grid.blocks[Location(3, 1)].pretty_format())
        # raise('Not solved!')
    else:
        to_add = int(
            str(grid.get_cell(Location(1, 1)).get_value()) +
            str(grid.get_cell(Location(2, 1)).get_value()) +
            str(grid.get_cell(Location(3, 1)).get_value())
        )
        print(to_add)
        # print(grid.pretty_format())
        sum += to_add
    # break

# print(grid.pretty_format_possibilities())

print(sum)
pt()