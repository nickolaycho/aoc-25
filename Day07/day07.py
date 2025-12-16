from functools import cached_property
from enum import StrEnum
from functools import lru_cache

class CellType(StrEnum):
    START = "S"
    BEAM = "|"
    EMPTY = "."
    SPLITTER = "^"

class Manifold():
    def __init__(self,
        lines: list[str]) -> None:
        self.lines: list[str] = lines
        self.num_rows:int = len(self.lines)
        self.num_columns: int = len(self.lines[0])
        first_line_updated: str = lines[0].replace(CellType.START, CellType.BEAM)
        self.updated_manifold: list[str] = [first_line_updated] + lines[1:]
        self.draw_beam_flow()
        self.cell_where_beam_starts: int = int([
            i for i,c in enumerate(self.lines[0]) if c==CellType.START
            ][0])

    @cached_property
    def num_possible_paths(self) -> int:
        return len(set(self.compute_all_possible_paths()))

    def compute_all_possible_paths(
        self,
        from_cell: tuple[int, int] | None = None,
        path: list[int] | None = None,
        all_paths: list[tuple[int, ...]] | None = None,
    ) -> list[tuple[int, ...]]:
        if from_cell is None:
            from_cell = (0, self.cell_where_beam_starts)
        if path is None:
            path = [self.cell_where_beam_starts]
        if all_paths is None:
            all_paths = []

        i, j = from_cell

        if i == self.num_rows - 1:
            all_paths.append(tuple(path))
            return all_paths

        cell_below_current: str = self.updated_manifold[i+1][j]
        beam_continuation: list[int] = []
        if cell_below_current==CellType.BEAM:
            beam_continuation.append(j)
        elif cell_below_current==CellType.SPLITTER:
            beam_continuation.extend([j-1,j+1])
        else:
            raise ValueError("Cell below beam must contain either beam or splitter")

        for cell_index in beam_continuation:
            self.compute_all_possible_paths(
                from_cell=(i + 1, cell_index),
                path=path + [cell_index],
                all_paths=all_paths,
            )

        return all_paths

    @cached_property
    def num_splits(self) -> int:
        num_splits: int=0
        for i in range(1, self.num_rows):
            for j in range(self.num_columns):
                if self.updated_manifold[i][j]==CellType.SPLITTER:
                    if self.updated_manifold[i-1][j]==CellType.BEAM:
                        num_splits += 1
        return num_splits   

    def draw_beam_flow(self) -> None:
        for i in range(self.num_rows-1):
            self.move_beam_downward(from_row_index=i)
        
    def move_beam_downward(self, from_row_index: int) -> None:
        from_row: str = self.updated_manifold[from_row_index]
        to_row_index: int = from_row_index + 1
        to_row: str = self.updated_manifold[to_row_index]
        beam_location: list[int] = [i for i, cell in enumerate(from_row)
                                     if cell==CellType.BEAM]
        next_row_beam_location: list[int] = []
        
        for cell_index in beam_location:
            if to_row[cell_index]==CellType.SPLITTER:
                next_row_beam_location.extend([cell_index-1, cell_index+1])
            elif to_row[cell_index]==CellType.EMPTY:
                next_row_beam_location.append(cell_index)
            else:
                raise ValueError("Cell can only be SPLITTER ('^') or EMPTY ('.')")
        
        next_row_beam_location = list(set(next_row_beam_location))
        for cell_index in next_row_beam_location:
            self.updated_manifold[to_row_index]=(
                self.updated_manifold[to_row_index][:cell_index] + 
                CellType.BEAM + 
                self.updated_manifold[to_row_index][cell_index+1:]
            )




    


