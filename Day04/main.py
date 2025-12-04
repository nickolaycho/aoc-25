from day04 import *

def main():

    input_path = "input.txt"
    input_file = get_input(input_path)

    grid = Grid(input_file=input_file)
    result = grid.count_accessible_rolls_of_paper()
    print("Part 1 result:", result)

    print("Part 2 result:")
    grid.remove_rolls_in_cycles()

if __name__ == "__main__":
    main()