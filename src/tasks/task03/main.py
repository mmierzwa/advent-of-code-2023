import sys
import re
from __future__ import annotations


class PartNumber:
    def __init__(self, row: int, column: int, value: int, length: int) -> None:
        self.row = row
        self.column = column
        self.value = value
        self.length = length

    @staticmethod
    def from_line(line: str, row: int) -> list[PartNumber]:
        parts: list[PartNumber] = []

        for match in re.finditer('\d+', line):
            part: PartNumber = PartNumber(row, match.start(), int(match.string), len(match.string))
            parts.append(part)

        return parts

    def get_neighbours(self) -> list[tuple[int]]:
        pass

class Symbol:
    def __init__(self, row: int, column: int) -> None:
        self.row = row
        self.column = column

    @staticmethod
    def from_line(line: str, row: int) -> list[Symbol]:
        symbols: list[Symbol] = []

        for match in re.finditer('', line):
            symbol: Symbol = Symbol(row, match.start())

        return symbols

class SchematicMap:
    def __init__(self) -> None:
        self.parts: dict[str, PartNumber] = {}
        self.symbols: set[str] = {}

    def add_from_line(self, line: str, row: int) -> None:
        for part in PartNumber.from_line(line, row):
            self.parts[f'{part.row}:{part.column}'] = part

        for symbol in Symbol.from_line(line, row):
            self.symbols.add(f'{symbol.row}:{symbol.column}')

def main() -> None:
    args = sys.argv[1:]

    if len(args) < 1:
        print("input file name required", file=sys.stderr)
        sys.exit(-1)

    input_filename = args[0]

    with open(input_filename, 'r') as input_file:
        for l in input_file:
            pass


if __name__ == '__main__':
    main()