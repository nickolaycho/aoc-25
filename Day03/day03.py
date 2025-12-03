from abc import ABC
from functools import cached_property
import re


class Day3(ABC):
    def __init__(self,
                 input_path: str="input.txt"):
        self.input_path: str = input_path

    @cached_property
    def input(self) -> list[str]:
        with open(self.input_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]


class Part1(Day3):

    def regex_to_find_matches(self, number: int) -> str:
        starts_with: str = str(number)[0]
        ends_with: str = str(number)[1]
        return rf"{starts_with}.*?{ends_with}"

    def bank_contains_number(self,
         bank: str,
         number: int) -> bool:
        return re.search(
            pattern=self.regex_to_find_matches(
                number=number),
            string=bank) is not None

    def bank_largest_joltage(self, bank: str):
        for i in range(100, 9, -1):
            if self.bank_contains_number(
                    bank=bank,
                    number=i):
                return i
        return -1

    def solve(self):
        total_output_joltage = 0
        for row in self.input:
            print(self.bank_largest_joltage(bank=row))
            total_output_joltage += self.bank_largest_joltage(
                bank=row
            )
        return total_output_joltage




class Part2(Day3):
    pass