from dataclasses import dataclass
from functools import cached_property
from tqdm import tqdm
from abc import ABC, abstractmethod
from utils import get_input

class PreprocessStrategy(ABC):
    @abstractmethod
    def get_numbers(self,
        input_lines: list[str]
    ) -> list[list[int]]:
        pass

class Part1PreprocessStrategy(PreprocessStrategy):
    def get_numbers(self, input_lines):
        numbers: list[list[int]]
        for line in input_lines[:-1]:
            self.numbers.append([int(num) for num in line.split()])
        return numbers

class Part2PreprocessStrategy(PreprocessStrategy):
    def get_numbers(self, input_lines) -> list[list[str]]:
        num_cols: int = max([len(line) for line in input_lines])
        all_numbers: list[list[int]] = []
        numbers_group: list[int] = []

        for col in range(num_cols):
            number: str = ""
            for line in input_lines[:-1]:
                number += line[col].strip()
            if number:
                numbers_group.append(int(number))
                print(number)
            else:
                all_numbers.append(numbers_group)
                numbers_group = []

        return all_numbers
    
class ColumnSolver(ABC):
    @abstractmethod
    def calculate_column_result(self,
            numbers: list[list[int]],
            symbol: str) -> int:
        pass

class StandardColumnSolver(ColumnSolver):

    def calculate_column_result(self,
            numbers: list[list[int]],
            symbol: str) -> int:
        if symbol == "*":
            return self.multiply_numbers(numbers)
        elif symbol == "+":
            return sum(numbers)
        else:
            raise ValueError(f"Unknown symbol: {symbol}")
        
    def multiply_numbers(self, numbers: list[int]) -> int:
        result = 1
        for num in numbers:
            result *= num
        return result

class Homework():
    def __init__(self,
                 input_file: list[str],
                 preprocess_strategy: PreprocessStrategy,
                 column_solver: ColumnSolver
                 ) -> None:
        self.input_file = input_file
        self.column_solver = column_solver
        self.preprocess_strategy = preprocess_strategy

        self.numbers: list[list[int]] = self.preprocess_strategy.get_numbers(
            input_lines=get_input(input_path=self.input_file)
        )

        self.num_of_columns: int = len(self.numbers[0])
        self.symbols: list[str] = self.input_file[-1].split()

    @cached_property
    def part_1_result(self) -> int:
        result: int = 0
        for column_index in range(self.num_of_columns):
            numbers: list[int] = [row[column_index] for row in self.numbers]
            symbol: str = self.symbols[column_index]
            col_result: int = self.column_solver.calculate_column_result(
                numbers=numbers,
                symbol=symbol
            )
            result += col_result
        return result

def part_2_preprocess(input_lines: list[str]) -> list[list[int]]:

    num_cols: int = max([len(line) for line in input_lines])
    all_numbers: list[list[int]] = []
    numbers_group: list[int] = []

    for col in range(num_cols):
        number: str = ""
        for line in input_lines[:-1]:
            number += line[col].strip()
        if number:
            numbers_group.append(int(number))
            print(number)
        else:
            all_numbers.append(numbers_group)
            numbers_group = []

    return all_numbers
            
