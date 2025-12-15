from functools import cached_property
from Day06.preprocess_strategy import *
from Day06.column_solver_strategy import *

class Homework():
    def __init__(self,
                 input_lines: list[str],
                 preprocess_strategy: PreprocessStrategy,
                 column_solver: ColumnSolver
                 ) -> None:
        self.input_lines = input_lines
        self.preprocess_strategy = preprocess_strategy
        self.column_solver = column_solver
        
        self.numbers: list[list[int]] = self.preprocess_strategy.get_numbers(
            input_lines=self.input_lines)
        self.num_of_columns: int = len(self.numbers)
        self.symbols: list[str] = self.input_lines[-1].split()

    @cached_property
    def result(self) -> int:
        result: int = 0
        for column_index in range(self.num_of_columns):
            numbers: list[int] = self.numbers[column_index]
            symbol: str = self.symbols[column_index]
            col_result: int = self.column_solver.calculate_column_result(
                numbers=numbers,
                symbol=symbol
            )
            result += col_result
        return result