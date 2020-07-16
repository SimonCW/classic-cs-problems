from dataclasses import dataclass
from typing import List
from enum import Enum
import random


class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"


@dataclass
class MazeLocation:
    row: int
    col: int


class Maze:
    def __init__(
        self,
        rows: int = 10,
        cols: int = 10,
        sparseness: float = 0.2,
        start: MazeLocation = MazeLocation(0, 0),
        goal: MazeLocation = MazeLocation(9, 9),
    ):
        self._rows: int = rows
        self._cols: int = cols
        self.start: MazeLocation = start
        self.goal: MazeLocation = goal
        # populate grid with empty cells
        self._grid: List[List[Cell]] = [
            [Cell.EMPTY for c in range(cols)] for r in range(rows)
        ]
        # populate with blocked cells
        self._randomly_fill(rows, cols, sparseness)
        # Fill start and goal
        self._grid[start.row][start.col] = Cell.START
        self._grid[goal.row][goal.col] = Cell.GOAL

    def _randomly_fill(self, rows: int, cols: int, sparseness: float):
        for row in range(rows):
            for col in range(cols):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][col] = Cell.BLOCKED

    def __str__(self) -> str:
        output: str = ""
        for row in self._grid:
            output += "".join([c.value for c in row]) + "\n"
        return output

    def goal_test(self, ml: MazeLocation) -> bool:
        return ml == self.goal

    def succesors(self, ml: MazeLocation) -> List[MazeLocation]:
        locations: List[MazeLocation] = []
        if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.col] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row + 1, ml.col))
        if ml.row - 1 >= 0 and self._grid[ml.row - 1][ml.col] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row - 1, ml.col))
        if ml.col + 1 < self._cols and self._grid[ml.row][ml.col + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.col + 1))
        if ml.col - 1 >= 0 and self._grid[ml.row][ml.col - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.col - 1))
        return locations


if __name__ == "__main__":
    maze = Maze()
    print(maze)
    print(maze.goal_test(MazeLocation(9, 9)))
