from Day06_Strategy_pattern.day06 import *
from utils import get_input_raw, get_input
from pathlib import Path

class TestDay6:
    def setup_method(self, method):
        here = Path(__file__).resolve().parent
        input_path = here / "test_input.txt"

        self.input_lines: list[str] = get_input(input_path=input_path)
        self.test_homework: Homework = Homework(
            input_lines=self.input_lines,
            preprocess_strategy=Part1PreprocessStrategy(),
            column_solver=StandardColumnSolver())

    def test_standard_column_solver(self):
        assert self.test_homework.column_solver.calculate_column_result(
            numbers=[123, 45, 6],
            symbol="*"
        )  == 33210
        assert self.test_homework.column_solver.calculate_column_result(
            numbers=[328, 64, 98],
            symbol="+"    
        ) == 490
        assert self.test_homework.column_solver.calculate_column_result(
            numbers=[51, 387, 215],
            symbol="*"
        ) == 4243455
        assert self.test_homework.column_solver.calculate_column_result(
            numbers=[64, 23, 314],
            symbol="+"
        ) == 401
    
    def test_part_1(self):
        assert self.test_homework.numbers==[[123, 45, 6], [328, 64, 98], [51, 387, 215], [64, 23, 314]]
        assert self.test_homework.result == 4277556

    def test_part_2(self):
        here = Path(__file__).resolve().parent
        input_path = here / "test_input.txt"
        input_lines = get_input_raw(input_path=input_path)

        homework_part_2 = Homework(
            input_lines=input_lines,
            preprocess_strategy=Part2PreprocessStrategy(),
            column_solver=StandardColumnSolver()
        )

        assert homework_part_2.numbers == [[1, 24, 356], [369, 248, 8], [32, 581, 175], [623, 431, 4]]
        assert homework_part_2.column_solver.calculate_column_result(
            numbers=[1, 24, 356], symbol="*")==8544
        assert homework_part_2.column_solver.calculate_column_result(
            numbers=[369, 248, 8], symbol="+")==625
        assert homework_part_2.column_solver.calculate_column_result(
            numbers=[32, 581, 175], symbol="*")==3253600
        assert homework_part_2.column_solver.calculate_column_result(
            numbers=[623, 431, 4], symbol="+")==1058

        assert homework_part_2.result == 3263827