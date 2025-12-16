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

    @property
    def num_possible_paths(self) -> int:
        return self.count_timelines(0, self.cell_where_beam_starts)

    @lru_cache(maxsize=None)
    def count_timelines(self,
            i: int,
            j: int) -> int:
        if i == self.num_rows - 1:
            return 1

        cell_below: str = self.updated_manifold[i+1][j]

        if cell_below == CellType.BEAM:
            return self.count_timelines(i+1, j)

        elif cell_below == CellType.SPLITTER:
            # timelines(i,j)=timelines(i+1,j−1)+timelines(i+1,j+1)
            num_paths_from_splitter: int = 0
            if j > 0: # potrebbe esserci uno splitter sul bordo sx
                num_paths_from_splitter += self.count_timelines(i+1, j-1)
            if j < self.num_columns - 1: # potrebbe esserci uno splitter sul bordo dx
                num_paths_from_splitter += self.count_timelines(i+1, j+1)
            return num_paths_from_splitter

        else:
            raise ValueError("Invalid cell")

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




    


