from petur import utils


def align_crabs_constant(input_list: list, target_position: int) -> int:
    total_changes = 0
    for crab_position in input_list:
        total_changes += abs(crab_position - target_position)

    return total_changes


def align_crabs_expensive(input_list: list, target_position: int) -> int:
    pass


def part1(input_file):
    int_list = utils.read_int_from_single_line_to_list(input_file)
    max_position = max(int_list)

    smallest_position = None
    smallest_movements = None
    for outcome in range(max_position):
        outcome_movements = align_crabs_constant(int_list, outcome)

        # first pass
        if (not smallest_position) or (outcome_movements < smallest_movements):
            smallest_position = outcome
            smallest_movements = outcome_movements

    print(f"smallest_position: {smallest_position}")
    print(f"smallest_movements: {smallest_movements}")


EXAMPLE_INPUT = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

# part 1
assert align_crabs_constant(EXAMPLE_INPUT, 2) == 37, "LOL"
assert align_crabs_constant(EXAMPLE_INPUT, 1) == 41, "LOL"
assert align_crabs_constant(EXAMPLE_INPUT, 3) == 39, "LOL"
assert align_crabs_constant(EXAMPLE_INPUT, 10) == 71, "LOL"

# part 2
assert align_crabs_expensive(EXAMPLE_INPUT, 5) == 168, "LOL"
assert align_crabs_expensive(EXAMPLE_INPUT, 2) == 206, "LOL"


if __name__ == "__main__":
    input_file = "input"
    part1(input_file)
