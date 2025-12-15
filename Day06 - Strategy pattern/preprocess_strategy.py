from abc import ABC, abstractmethod

class PreprocessStrategy(ABC):
    @abstractmethod
    def get_numbers(self,
        input_lines: list[str]
    ) -> list[list[int]]:
        raise NotImplementedError

class Part1PreprocessStrategy(PreprocessStrategy):
    def get_numbers(self, input_lines: list[str])-> list[list[int]]:
        horizontal_numbers: list[list[int]] = self.horizontal_numbers(
            input_lines=input_lines)
        num_of_columns = len(horizontal_numbers[0])
        all_numbers: list[list[int]] = []

        for column_index in range(num_of_columns):
            all_numbers.append([row[column_index] for row in horizontal_numbers])   
        return all_numbers
    
    def horizontal_numbers(self, input_lines: list[str]) -> list[list[int]]:
        horizontal_numbers: list[list[int]] = []
        for line in input_lines[:-1]:
            horizontal_numbers.append([int(num) for num in line.split()])
        return horizontal_numbers

class Part2PreprocessStrategy(PreprocessStrategy):
    def get_numbers(self, input_lines: list[str]) -> list[list[str]]:
        num_cols: int = max([len(line) for line in input_lines])
        all_numbers: list[list[int]] = []
        numbers_group: list[int] = []

        for col in range(num_cols):
            number: str = ""
            for line in input_lines[:-1]:
                number += line[col].strip()
            if number:
                numbers_group.append(int(number))
            else:
                all_numbers.append(numbers_group)
                numbers_group = []
        return all_numbers
    