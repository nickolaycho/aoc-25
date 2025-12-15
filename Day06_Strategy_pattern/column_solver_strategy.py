from abc import ABC, abstractmethod

class ColumnSolver(ABC):
    @abstractmethod
    def calculate_column_result(self,
            numbers: list[list[int]],
            symbol: str) -> int:
        raise NotImplementedError

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
        result: int = 1
        for num in numbers:
            result *= num
        return result
