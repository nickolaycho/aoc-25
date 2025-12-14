from Day06.day06 import *
from utils import get_input_raw

class TestDay6:
    def setup_method(self, method):
        self.input_path = "test_input.txt"
        self.input = get_input(input_path=self.input_path)
        self.test_homework = Homework(
            input_file=self.input,
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
        assert self.test_homework.part_1_result == 4277556

    def test_part_2(self):
        input_path = "test_input.txt"
        input = get_input_raw(input_path=input_path)
        part_2_result = part_2_preprocess(
            input_lines=[line for line in input if line]
        )
        print(part_2_result)
        assert 2==0