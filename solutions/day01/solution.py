from petur import utils


def count_number_of_larger(input_list):
    larger_count = 0
    for index, number in enumerate(input_list):
        if index == 0:
            continue
        previous_number = input_list[index - 1]

        if number > previous_number:
            larger_count += 1
    return larger_count


def count_number_of_three_larger(input_list):
    larger_count = 0
    for index, number in enumerate(input_list):
        if index <= 2:
            continue
        current_range = input_list[index - 2 :][:3]
        previous_range = input_list[index - 3 :][:3]

        if sum(current_range) > sum(previous_range):
            larger_count += 1
    return larger_count


EXAMPLE_INPUT = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
assert count_number_of_larger(EXAMPLE_INPUT) == 7, "LOL"
assert count_number_of_three_larger(EXAMPLE_INPUT) == 5, "LOL"


if __name__ == "__main__":
    input = "input"
    input_list = utils.read_multi_line_ints_to_list(input)

    print("=== PART 1 ===")
    part1_count = count_number_of_larger(input_list)
    print(part1_count)

    print("=== PART 2 ===")
    part2_count = count_number_of_three_larger(input_list)
    print(part2_count)
