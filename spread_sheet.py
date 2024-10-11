from enum import Enum
class CellOps(Enum):
    ADD = '+'
    SUB = '-'
    MUL = '*'
    DIV = '/'

def run_calculator(num1, num2, op):
    if CellOps(op) == CellOps.ADD:
        return num1 + num2
    elif CellOps(op) == CellOps.SUB:
        return num1 - num2
    elif CellOps(op) == CellOps.MUL:
        return num1 * num2
    elif CellOps(op) == CellOps.DIV:
        if num2 != 0:
            return num1 / num2
        else:
            return 0

class SpreadSheet:
    def __init__(self):
        self.cells = {}

    def get_cell_value(self, cell):
        return self.cells[cell]

    def set_cell_value(self, cell, value):
        if type(value) == tuple:
            op,num1,num2 = value
            if self.cells[num1] and self.cells[num2]:
                self.cells[cell] = run_calculator(self.cells[num1], self.cells[num2], op)
            else:
                raise Exception("Cell doesn't exist")
        else:
            self.cells[cell] = value


def main():
    spread_sheet = SpreadSheet()
    spread_sheet.set_cell_value((0, 0), 1.0)
    spread_sheet.set_cell_value((0, 1), 2.0)
    spread_sheet.set_cell_value((1, 0), 3.0)
    spread_sheet.set_cell_value((1, 1), ('/', (0, 0), (0, 1)))

    print(spread_sheet.get_cell_value((1, 1)))
          
if __name__ == '__main__':
    main()