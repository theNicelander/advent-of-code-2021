def read_data_into_list(path: str) -> list:
    with open(path) as f:
        return f.read().splitlines()


def read_multi_line_ints_to_list(path: str) -> list:
    str_list = read_data_into_list(path)
    return [int(num) for num in str_list]


def read_groups_into_list(path: str) -> list:
    """
    Reads multiple lines of strings, separated by newline into a single string.
    Treat the as groups if separated by empty new lines
    Args:
        path: path to file
    Returns:
        list of concatenated strings, grouped together by an empty new line
    Example input:
        abc
        def
        g
    Example output:
        ["abcdef", "g"]
    """
    with open(path) as f:
        raw_groups = f.read().split("\n\n")
    return [g.replace("\n", "") for g in raw_groups]


def read_int_from_single_line_to_list(path):
    input_string = read_data_into_list(path)[0]
    int_list = [int(num) for num in input_string.split(",")]
    return int_list
