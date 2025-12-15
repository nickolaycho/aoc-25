from Day06_Strategy_pattern.day06 import *
import time
from utils import get_input, get_input_raw
from pathlib import Path

def main():

    here = Path(__file__).resolve().parent
    input_path = here / "input.txt"
    input_lines = get_input(input_path)

    homework_part_1 = Homework(
        input_lines=input_lines,
        preprocess_strategy=Part1PreprocessStrategy(),
        column_solver=StandardColumnSolver())

    start = time.perf_counter()
    part_1_result = homework_part_1.result
    end = time.perf_counter()
    print("Part 1 result: ", part_1_result)
    print(f"Part 1 time: {(end - start):.3f} s")

    print("*"*70)

    print("Part 2")

    input_lines = get_input_raw(input_path)

    homework_part_2 = Homework(
        input_lines=input_lines,
        preprocess_strategy=Part2PreprocessStrategy(),
        column_solver=StandardColumnSolver())
    
    start = time.perf_counter()
    part2_result = homework_part_2.result
    end = time.perf_counter()
    print("Part 2 result: ", part2_result)
    print(f"Part 2 time: {(end - start):.3f} s")

if __name__ == "__main__":
    main()