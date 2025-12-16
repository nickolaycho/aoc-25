from day11 import *
import time

def main():

    input_path = "input.txt"
    input_file = get_input(input_path)

    network: Network = Network(input_file=input_file)
    start = time.perf_counter()
    part_1_result = network.num_paths_to_you()
    end = time.perf_counter()
    print("Part 1 result: ", part_1_result)
    print(f"Part 1 time: {(end - start):.3f} s")

    print("Part 2")
    start = time.perf_counter()
    part2_result = None
    end = time.perf_counter()
    print("Part 2 result: ", part2_result)
    print(f"Part 2 time: {(end - start):.3f} s")


if __name__ == "__main__":
    main()