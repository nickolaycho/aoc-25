from Day07.day07 import *
import time
from pathlib import Path
from utils import get_input

def main():

    here = Path(__file__).resolve().parent
    input_path = here / "input.txt"
    input_lines = get_input(input_path)

    start = time.perf_counter()
    manifold = Manifold(lines=input_lines)
    part_1_result = manifold.num_splits
    end = time.perf_counter()
    print("Part 1 result: ", part_1_result)
    print(f"Part 1 time: {(end - start):.3f} s")

    print("Part 2")
    start = time.perf_counter()
    part2_result = manifold.num_possible_paths
    end = time.perf_counter()
    print("Part 2 result: ", part2_result)
    print(f"Part 2 time: {(end - start):.3f} s")


if __name__ == "__main__":
    main()