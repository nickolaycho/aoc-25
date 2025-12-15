from pathlib import Path
import time
from utils import get_input
from Day01.day01 import *

def main():
    here = Path(__file__).resolve().parent
    input_path = here / "input.txt"
    input_lines = get_input(input_path)

    part1 = Part1(input_lines=input_lines)
    print(part1.input_to_array())
    part1_result = part1.solve()
    print("Part 1:", part1_result)

    part2 = Part2(input_lines=input_lines)
    part2_result = part2.solve()
    print("Part 2:", part2_result)

if __name__ == "__main__":
    main()